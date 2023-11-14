"""Main module."""


import contextlib
import os
from typing import Callable, Any


def shhh(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Silence stdout. Use this as a decorator.

    Example:
    >>> @shhh
    >>> def my_loud_function(param1, param2):
    >>>     ...
    """

    def wrapper(*args, **kwargs):
        with open(os.devnull, "w") as student_output:
            with contextlib.redirect_stdout(student_output):
                return func(*args, **kwargs)
    return wrapper
