from love_letter.base_struct.task import *
from love_letter.objects import *

class LoveLetterDrawCardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__()
        
        self._player = player
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player
