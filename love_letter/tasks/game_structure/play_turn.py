from love_letter.base_struct.task import *
from love_letter.objects import *

class LoveLetterPlayTurnTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, turn_state: LoveLetterTurnState):
        super().__init__()

        self._player = player
        self._turn_state = turn_state
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_turn_state(self) -> LoveLetterTurnState:
        return self._turn_state
