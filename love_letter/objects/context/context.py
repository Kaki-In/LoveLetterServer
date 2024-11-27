from love_letter.board import *
from love_letter.states import *
from .configuration import *

import board_game as _board_game

class LoveLetterGameContext(_board_game.BoardGameContext):
    def __init__(self, board: LoveLetterBoard, state: LoveLetterGameState, configuration: LoveLetterConfiguration):
        super().__init__(board, state, configuration)

        self._board = board
        self._state = state
        self._configuration = configuration
    
    def get_board(self) -> LoveLetterBoard:
        return self._board
    
    def get_state(self) -> LoveLetterGameState:
        return self._state
    
    def get_configuration(self) -> LoveLetterConfiguration:
        return self._configuration

