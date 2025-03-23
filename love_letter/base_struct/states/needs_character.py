from love_letter.board import *
from .state import *

import typing as _T

class LoveLetterNeedingCharacterState(LoveLetterState):
    def __init__(self, possibilities: list[LoveLetterCharacter]):
        LoveLetterState.__init__(self)

        self._character: _T.Optional[LoveLetterCharacter] = None
        self._possibilities = possibilities

    def get_chosen_character(self) -> LoveLetterCharacter:
        if self._character is None:
            raise TypeError("this state has not been given a player yet")

        return self._character
    
    def set_chosen_character(self, character: LoveLetterCharacter):
        self._character = character

    def has_chosen_character(self) -> bool:
        return self._character is not None
    
    def get_chosable_characters(self) -> list[LoveLetterCharacter]:
        return self._possibilities.copy()

