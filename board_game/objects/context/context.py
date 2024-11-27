from .board import *
from .state import *
from .configuration import *

class BoardGameContext():
    def __init__(self, board: BoardGameBoard, state: BoardGameState, configuration: BoardGameConfiguration):
        self._board = board
        self._state = state
        self._configuration = configuration
    
    def get_board(self) -> BoardGameBoard:
        return self._board
    
    def get_state(self) -> BoardGameState:
        return self._state
    
    def get_configuration(self) -> BoardGameConfiguration:
        return self._configuration

