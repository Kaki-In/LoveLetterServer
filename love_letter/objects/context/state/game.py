from .round import *

import typing as _T

class LoveLetterGameState():
    def __init__(self):
        self._round_state: _T.Optional[LoveLetterRoundState] = None
    
    def is_initialized(self) -> bool:
        return self._round_state is not None
    
    def initialize(self, first_round_state: LoveLetterRoundState) -> None:
        self._round_state = first_round_state

    def get_round_state(self) -> LoveLetterRoundState:
        if self._round_state is None:
            raise ValueError('this game has not been initialized yet')
        
        return self._round_state
        

