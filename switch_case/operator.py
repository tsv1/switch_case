import operator
from typing import Any, Callable

from .curry import curry
from .infix import Infix


class Operator:
    def __eq__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.eq, other)

    def __ne__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.ne, other)

    def __lt__(self, other: Any) -> Callable[[Any], bool]:
        return curry(operator.lt, other)

    def __le__(self, other: Any) -> Callable[[Any], bool]:
        return curry(operator.le, other)

    def __gt__(self, other: Any) -> Callable[[Any], bool]:
        return curry(operator.gt, other)

    def __ge__(self, other: Any) -> Callable[[Any], bool]:
        return curry(operator.ge, other)

    def __call__(self, fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[..., Any]:
        return curry(fn, *args, **kwargs)

    def __truediv__(self, other: Any) -> Infix:
        return Infix(other)
