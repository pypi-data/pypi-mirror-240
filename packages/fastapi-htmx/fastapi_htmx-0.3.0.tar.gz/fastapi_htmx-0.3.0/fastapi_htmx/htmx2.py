import inspect
import logging
from collections.abc import Callable, Mapping
from functools import wraps
from typing import Optional

from fastapi import Request
from fastapi.templating import Jinja2Templates

from fastapi_htmx.htmx import _is_fullpage_request, MissingFullPageTemplateError, MissingHTMXInitError


class HTMXExtension:  # noqa: D101
    _templates_path = None
    _htmx_decorator = None

    @staticmethod
    def init(templates: Jinja2Templates):  # noqa: D102
        # FIXME: learn more about decorator functions and check how to use them and if this actually works with the suggestion from chatgpt
        pass

        HTMXExtension._htmx_decorator = htmx_decorator_factory()

    @staticmethod
    def htmx(  # noqa: D102
        partial_template_name: str,
        full_template_name: Optional[str] = None,
        # ... other parameters ...
    ):
        if HTMXExtension._htmx_decorator is None:
            raise Exception("HTMX Extension not initialized. Call HTMXExtension.initialize() first.")
        return HTMXExtension._htmx_decorator(partial_template_name, full_template_name, ...)
