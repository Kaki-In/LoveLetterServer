from love_letter.objects import *
from .game import *

import board_game.base_struct.criteria as _board_game_criteria

class LoveLetterCriteria(_board_game_criteria.BoardGameCriteria):
    def __init__(self):
        _board_game_criteria.BoardGameCriteria.__init__(self)
        self._game_criteria = LoveLetterGameCriteria()
    
    def get_game_criteria(self) -> LoveLetterGameCriteria:
        return self._game_criteria


