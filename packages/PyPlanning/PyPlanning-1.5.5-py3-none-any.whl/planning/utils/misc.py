# -*- coding: utf-8 -*-

"""
PyPlanning Miscelleneous utilities
"""

from __future__ import annotations

from collections.abc import Callable
from contextlib import contextmanager
from dataclasses import dataclass


def to_string(obj):
    """Convert to string, trying utf-8 then latin-1 codec"""
    if isinstance(obj, bytes):
        try:
            return obj.decode()
        except UnicodeDecodeError:
            return obj.decode("latin-1")
    try:
        return str(obj)
    except UnicodeDecodeError:
        return str(obj, encoding="latin-1")


@dataclass
class ExceptionContextData:
    """Object representing exception context data"""

    # Exception classes tuple: exceptions that should be considered harmless in the
    # context of the exception context manager, and would trigger a call to
    # the exception_callback function.
    exception_classes: list | tuple
    # Exception callback: function to call when an exception is raised.
    exception_callback: Callable


@contextmanager
def exception_context(data: ExceptionContextData) -> None:
    """Exception context manager

    This context manager is used to catch exceptions and call a callback function
    when an exception is raised. The callback function is called only if the
    exception is not in the tuple of harmless exceptions.
    """
    try:
        yield
    except tuple(data.exception_classes) as exc:
        data.exception_callback(exc)
