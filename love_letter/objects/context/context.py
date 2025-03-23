from love_letter.board import *
from love_letter.states import *
from love_letter.configuration import *

import board_game as _board_game

class LoveLetterGameContext(_board_game.BoardGameContext):
    def __init__(self, board: LoveLetterBoard, configuration: LoveLetterConfiguration):
        _board_game.BoardGameContext.__init__(self, board, configuration)

        self._board = board
        self._configuration = configuration
    
    def get_board(self) -> LoveLetterBoard:
        return self._board
    
    def get_configuration(self) -> LoveLetterConfiguration:
        return self._configuration

