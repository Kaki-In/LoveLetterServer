import typing as _T

from ..reason import *

class LoveLetterClientMessage():
    def __init__(self, name: str, args: dict[str, _T.Any]):
        self._name = name
        self._args = args
    
    def toJson(self) -> dict[str, _T.Any]:
        return {
            "name": self._name,
            "args": self._args
        }
    
    def get_name(self):
        return self._name
    
    def get_args(self):
        return self._args
