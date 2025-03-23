from board_game.board import *
from .configuration import *

class BoardGameContext():
    def __init__(self, board: BoardGameBoard, configuration: BoardGameConfiguration):
        self._board = board
        self._configuration = configuration
    
    def get_board(self) -> BoardGameBoard:
        return self._board
    
    def get_configuration(self) -> BoardGameConfiguration:
        return self._configuration

