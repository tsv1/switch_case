from typing import Any, List

from .case import Case


class Switch:
    def __init__(self, cases: List[Case] = []) -> None:
        self._cases = cases

    def __or__(self, case: Case) -> "Switch":
        return Switch(self._cases + [case])

    def __call__(self, smth: Any) -> Any:
        for case in self._cases:
            if case.match(smth):
                return case.resolve()
        raise ValueError(smth)
