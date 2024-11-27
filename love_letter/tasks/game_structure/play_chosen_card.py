from love_letter.base_struct.task import *
from love_letter.objects import *

from love_letter.states import *

class LoveLetterPlayChosenCardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, card_state: LoveLetterNeedingCardState) -> None:
        self._player = player

        self._card_state = card_state

    def get_player(self) -> LoveLetterPlayer:
        return self._player

    def get_chosen_card_state(self) -> LoveLetterNeedingCardState:
        return self._card_state


