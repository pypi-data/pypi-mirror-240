import asyncio
import datetime
from typing import Any


def get_or_create_event_loop():
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        # Create a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop


def get_thread_context():
    loop = get_or_create_event_loop()
    context = [asyncio.current_task(loop=loop)]
    return hash(tuple(context))


def clean_attribute(attribute: str):
    """
    Normalize attribute names for shorthand and work arounds for limitations
    in Python's syntax
    """

    # Shorthand
    attribute = {
        "cls": "class",
        "className": "class",
        "class_name": "class",
        "klass": "class",
        "fr": "for",
        "html_for": "for",
        "htmlFor": "for",
        "phor": "for",
    }.get(attribute, attribute)

    # Workaround for Python's reserved words
    if attribute != "_" and attribute[0] == "_":
        attribute = attribute[1:]

    # Workaround for dash
    special_prefix = any(
        attribute.startswith(x)
        for x in (
            "data_",
            "aria_",
            # htmx
            "hx_",
            # alpine
            "x_",
        )
    )
    if attribute in {"http_equiv"} or special_prefix:
        attribute = attribute.replace("_", "-").lower()

    # if starts and ends with _, replace the first with a : and remove the last
    if attribute.startswith("_") and attribute.endswith("__"):
        attribute = attribute.replace("_", ":", 1).replace("__", "")

    # replace with @
    if attribute != "_" and attribute.startswith("_"):
        attribute = attribute.replace("_", "@")

    if attribute.startswith("hx-"):
        # : is for javascript events
        # :: is for htmx events
        attribute = attribute.replace("---", "::").replace("--", ":")

    # Workaround for colon
    if attribute.split("_")[0] in ("xlink", "xml", "xmlns"):
        attribute = attribute.replace("_", ":", 1).lower()

    return attribute


def escape(data: Any, quote=True):  # stolen from std lib cgi # type: ignore
    """
    Escapes special characters into their html entities
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true, the quotation mark character (")
    is also translated.

    This is used to escape content that appears in the body of an HTML document
    """
    # Addition to convert ints to strings
    if isinstance(data, (int, float, bool, complex)):
        data = str(data)
    elif isinstance(data, datetime.datetime):
        # convert to en-US format, on the system timezone
        data = data.strftime("%m/%d/%Y %H:%M:%S")
    elif isinstance(data, datetime.date):
        data = data.strftime("%m/%d/%Y")
    elif data is None:
        data = ""
    data = data.replace("&", "&amp;")  # Must be done first!
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    if quote:
        data = data.replace('"', "&quot;")
    return data
