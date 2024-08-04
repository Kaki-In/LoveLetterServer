from .board import *
from .state import *
from .configuration import *

class LoveLetterGameContext():
    def __init__(self, board: LoveLetterBoard, state: LoveLetterGameState, configuration: LoveLetterConfiguration):
        self._board = board
        self._state = state
        self._configuration = configuration
    
    def get_board(self) -> LoveLetterBoard:
        return self._board
    
    def get_state(self) -> LoveLetterGameState:
        return self._state
    
    def get_configuration(self) -> LoveLetterConfiguration:
        return self._configuration

