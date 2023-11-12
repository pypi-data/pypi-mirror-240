import json
from typing import Any, Optional

import dominate
import dominate.tags as t
from dominate.util import raw  # type: ignore
from fastapi import Request

from .env import env

SCRIPT_TAGS: list[Any] = []
"""Used to cache the script tags as this is only needed to be ran once and does not change"""


def load_script_tags() -> list[Any]:
    # Avoid unnecessary operations if SCRIPT_TAGS is not empty
    if SCRIPT_TAGS:
        return SCRIPT_TAGS

    from .build import build

    files = sorted(build.files.items())

    for file_name, file_hash in files:
        file_url = (
            f"{env.weba_public_url}/{file_name}"
            if file_hash == ""
            else f"{env.weba_public_url}/{file_name.rsplit('.', 1)[0]}-{file_hash}.{file_name.rsplit('.', 1)[1]}"
        )

        # Create a script tag with the file name and hash as key and value
        if file_url.endswith(".css"):
            SCRIPT_TAGS.append(
                t.link(
                    rel="stylesheet",
                    href=file_url,
                    type="text/css",
                )
            )
        elif file_url.endswith("._hs"):
            SCRIPT_TAGS.append(t.script(src=file_url, type="text/hyperscript"))
        else:
            SCRIPT_TAGS.append(t.script(src=file_url, type="text/javascript"))

    # FIXME: currently htmx boost does not update the body tag
    # https://github.com/bigskysoftware/htmx/issues/1384
    SCRIPT_TAGS.append(
        t.script(
            raw(
                f"""
                    document.addEventListener("DOMContentLoaded", function() {{
                        {'' if env.live_reload else 'htmx.logNone();'}
                        document.body.addEventListener('htmx:afterSwap', function(evt) {{
                            const parser = new DOMParser();
                            const parsedResponse = parser.parseFromString(evt.detail.xhr.response, "text/html");
                            const bodyAttributes = parsedResponse.getElementsByTagName('body')[0].attributes;
                            for (const attribute of bodyAttributes) {{
                                evt.detail.target.setAttribute(attribute.name, attribute.value);
                            }}
                        }});
                    }});
                 """
            )
        )
    )

    return SCRIPT_TAGS


class WebaDocument(dominate.document):
    body: t.body
    head: t.head

    def __init__(self, title: str = "Weba", doctype: str = "<!DOCTYPE html>", *args: Any, **kwargs: Any):
        self._weba_head_rendered = False
        super().__init__(*args, title=title, doctype=doctype, **kwargs)  # type: ignore

    def render(self, indent: str = "  ", pretty: bool = True, xhtml: bool = False):
        if not self._weba_head_rendered:
            self._render_default_head()

        return super().render(indent, pretty, xhtml)

    def _render_default_head(self) -> None:
        with self.head:
            t.meta(charset="utf-8")
            t.meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, "
                "user-scalable=no, viewport-fit=cover",
            )
            t.meta(name="htmx-config", content=f"{json.dumps(env.htmx_config)}")

        self.head.add(load_script_tags())  # type: ignore
        self._weba_head_rendered = True


def weba_document(request: Request) -> WebaDocument:
    return request.scope["weba_document"]


def get_document(
    doctype: str = "<!DOCTYPE html>",
    request: Optional[Request] = None,
    *args: Any,
    **kwargs: Any,
):
    doc = WebaDocument(*args, doctype=doctype, **kwargs)

    doc.body["hx-ext"] = ", ".join(env.htmx_extentions)

    doc.body["class"] = "overflow-x-hidden overflow-y-auto overscroll-y-none h-full"
    doc["class"] = "h-full"

    if request:
        request.session.setdefault("store", {})
        csrf_token = request.session.get("csrf_token", "")
        doc.body["hx-headers"] = f'{{"X-CSRF-Token": "{csrf_token}"}}'

    if env.htmx_boost:
        doc.body["hx-boost"] = "true"
        doc.body["hx-history"] = "false"

    if env.live_reload:
        doc.body["ws-connect"] = env.live_reload_url
        # TODO: Fix the build process to stop it loading assets multiple times
        # doc.body["hx-on"] = "htmx:wsClose: htmx.ajax('GET', window.location.href, null, {history: 'replace'});"
        doc.body["hx-on"] = "htmx:wsClose: window.location.reload();"

    return doc
