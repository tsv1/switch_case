from functools import wraps
from typing import Any, Callable


def curry(fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[..., Any]:
    @wraps(fn)
    def wrapped(*prefix_args: Any, **override_kwargs: Any) -> Any:
        return fn(*(prefix_args + args), **{**kwargs, **override_kwargs})
    return wrapped
