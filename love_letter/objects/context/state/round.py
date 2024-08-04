from .turn import *
from ..board import *

import typing as _T

class LoveLetterRoundState():
    def __init__(self):
        self._turn_state: _T.Optional[LoveLetterTurnState] = None

    def has_been_setup(self) -> bool:
        return self._turn_state is not None
    
    def mark_as_setupped(self, first_turn_state: LoveLetterTurnState) -> None:
        self._turn_state = first_turn_state
    
    def set_turn_state(self, turn: LoveLetterTurnState) -> None:
        self._turn_state = turn
    
    def get_turn_state(self) -> LoveLetterTurnState:
        if self._turn_state is None:
            raise ValueError('this round has not been initialized yet')

        return self._turn_state
    
