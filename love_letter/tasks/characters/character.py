from love_letter.base_struct.task import *
from love_letter.objects import *

class LoveLetterCharacterTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, board: LoveLetterBoard, configuration: LoveLetterConfiguration):
        self._player = player
        self._board = board
        self._configuration = configuration

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_effective_board(self) -> LoveLetterBoard:
        return self._board
    
    def get_effective_configuration(self) -> LoveLetterConfiguration:
        return self._configuration
