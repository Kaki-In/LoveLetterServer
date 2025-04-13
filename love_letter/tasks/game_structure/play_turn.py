from love_letter.base_struct.task import *
from love_letter.context import *
from love_letter.states import *

class LoveLetterPlayTurnTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, turn_state: LoveLetterTurnState):
        LoveLetterTask.__init__(self)

        self._player = player
        self._turn_state = turn_state
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_turn_state(self) -> LoveLetterTurnState:
        return self._turn_state
