from love_letter.base_struct.task import *
from love_letter.objects import *
from love_letter.states import *

class LoveLetterChooseCardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, state: LoveLetterNeedingCardState):
        super().__init__()
        self._effective_player = player
        self._state = state

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._effective_player
    
    def get_needing_card_state(self) -> LoveLetterNeedingCardState:
        return self._state
