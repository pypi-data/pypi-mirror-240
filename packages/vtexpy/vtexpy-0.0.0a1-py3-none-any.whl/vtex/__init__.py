from ._exceptions import RequestError, VTEXError
from ._response import VTEXResponse
from ._vtex import VTEX

__all__ = [
    "RequestError",
    "VTEX",
    "VTEXError",
    "VTEXResponse",
]


for name in __all__:
    locals()[name].__module__ = "vtex"
