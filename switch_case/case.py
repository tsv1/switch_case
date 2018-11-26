from typing import Any, Callable


class Case:
    def __init__(self, predicate: Callable[[Any], bool]) -> None:
        self._predicate = predicate

    def __rshift__(self, value: Any) -> "Case":
        self._value = value
        return self

    def match(self, expr: Any) -> bool:
        return self._predicate(expr)

    def resolve(self) -> Any:
        if not hasattr(self, "_value"):
            raise ValueError("case holds no value")
        return self._value
