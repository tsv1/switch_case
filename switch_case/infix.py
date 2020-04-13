from typing import Any, Callable

from .curry import curry


class Infix:
    def __init__(self, fn: Callable[..., Any]) -> None:
        self._fn = fn

    def __truediv__(self, arg: Any) -> Callable[..., Any]:
        return curry(self._fn, arg)
