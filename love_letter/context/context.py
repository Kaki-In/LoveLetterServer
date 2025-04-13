import board_game as _board_game

from love_letter.configuration import *
from love_letter.board import *

class LoveLetterContext(_board_game.BoardGameContext[LoveLetterConfiguration]):
    """
    Defines the context of the game.  
    """

    def __init__(self, configuration: LoveLetterConfiguration, board: LoveLetterBoard) -> None:
        self._configuration = configuration
        self._board = board

    def get_board(self) -> LoveLetterBoard:
        return self._board



