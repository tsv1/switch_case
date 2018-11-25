from typing import Any, Callable


class Operator:
    def __eq__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return lambda x: x == other

    def __ne__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return lambda x: x != other
