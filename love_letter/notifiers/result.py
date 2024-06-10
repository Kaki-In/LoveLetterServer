import typing as _T

class ClientMessage():
    def __init__(self, name: str, args: dict[str, _T.Any]):
        self._name = name
        self._args = args
    
    def toJson(self) -> dict[str, _T.Any]:
        return {
            "name": self._name,
            "args": self._args
        }
    
