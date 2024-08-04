from .task import *
from ...objects.context.board import *

class LoveLetterDrawCardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__()
        
        self._player = player
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player
