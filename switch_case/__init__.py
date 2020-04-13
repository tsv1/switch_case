from .case import Case
from .operator import Operator
from .switch import Switch

__all__ = ("switch", "case", "default", "_")
__version__ = "1.4"

switch = Switch()
case = lambda x: Case(x)  # noqa: E731
default = Case(lambda x: True)
_ = Operator()
