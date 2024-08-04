import typing as _T

class LoveLetterGameConfiguration():
    def __init__(self, max_rounds: _T.Optional[int]):
        self._max_rounds = max_rounds

    def has_max_rounds_imposed(self) -> bool:
        return self._max_rounds is not None
    
    def get_max_rounds(self) -> int:
        if self._max_rounds is None:
            raise ValueError('there is no max_rounds imposed')
        
        return self._max_rounds

