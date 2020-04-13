from typing import Any, List

from .case import Case
from .nil import Nil


class Switch:
    def __init__(self, cases: List[Case] = [], expr: Any = Nil) -> None:
        self._cases = cases
        self._expr = expr

    def __or__(self, case: Case) -> "Switch":
        return Switch(self._cases + [case], self._expr)

    def __call__(self, expr: Any = Nil) -> Any:
        if (expr is Nil) and (len(self._cases) == 0 or self._expr is Nil):
            raise ValueError("Too few arguments")
        if (expr is not Nil) and (self._expr is not Nil):
            raise ValueError("Too many arguments")

        if len(self._cases) == 0 and (expr is not Nil):
            return Switch(expr=expr)
        elif expr is Nil:
            expr = self._expr

        for case in self._cases:
            if case.match(expr):
                return case.resolve()

        raise ValueError(expr)

    def __invert__(self) -> Any:
        return self()
