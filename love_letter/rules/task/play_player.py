from .task import *
from ...objects.context.board import *

class LoveLetterPlayPlayerTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__()
        self._player = player
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
