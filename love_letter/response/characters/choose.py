import typing as _T
from love_letter.base_struct.response import *
from love_letter.enum import *
from love_letter.board import *

class LoveLetterChooseCharacterResponse(LoveLetterClientResponse):
    def __init__(self, character: LoveLetterCharacter):
        LoveLetterClientResponse.__init__(self)

        self._character = character

    def get_character(self) -> LoveLetterCharacter:
        return self._character
