from .message import *

from ..result import *

import typing as _T

class LoveLetterClientInteraction(LoveLetterClientMessage):
    def __init__(self, name: str, args: dict[str, _T.Any]):
        super().__init__(name, args)
        
        self._result: _T.Optional[LoveLetterClientResult] = None
    
    def has_anwser(self) -> bool:
        return self._result is not None
    
    def get_result(self) -> LoveLetterClientResult:
        if self._result is None:
            raise ValueError('result not received yet')
        
        return self._result
    
    def set_result(self, result: LoveLetterClientResult) -> None:
        if not self.answer_is_valid(result):
            raise ValueError('invalid result value')
        
        self._result = result
    
    def answer_is_valid(self, result: LoveLetterClientResult) -> bool:
        return result.get_name() == self._name
    
