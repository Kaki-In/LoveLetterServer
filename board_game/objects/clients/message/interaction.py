from .message import *

from ..result import *

import typing as _T

class BoardGameClientInteraction(BoardGameClientMessage):
    def __init__(self, name: str, args: dict[str, _T.Any]):
        super().__init__(name, args)
        
        self._result: _T.Optional[BoardGameClientResponse] = None
    
    def has_anwser(self) -> bool:
        return self._result is not None
    
    def get_result(self) -> BoardGameClientResponse:
        if self._result is None:
            raise ValueError('result not received yet')
        
        return self._result
    
    def set_result(self, result: BoardGameClientResponse) -> None:
        if not self.answer_is_valid(result):
            raise ValueError('invalid result value')
        
        self._result = result
    
    def answer_is_valid(self, result: BoardGameClientResponse) -> bool:
        return result.get_name() == self._name
    
