from .switch import Switch
from .case import Case
from .operator import Operator


__all__ = ("switch", "case", "default", "_")
__version__ = "1.2"

switch = Switch()
case = lambda x: Case(x)
default = Case(lambda x: True)
_ = Operator()
