from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

class LoveLetterDiscardRule(LoveLetterRule):
    def __init__(self, task: LoveLetterDiscardTask):
        super().__init__(task)

        self._card = task.get_card()
        self._reason = task.get_reason()
        self._player = task.get_effective_player()
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        if self._card == LOVE_LETTER_PLAYER_CARD.PLAYER_CARD:
            card = self._player.get_card()
            self._player.lay_card()
        else:
            card = self._player.get_drawn_card()
            self._player.lay_drawn_card()

        self._player.add_to_discard(card)

        return [
            LoveLetterDiscardAction(self._player, card, self._card, self._reason)
        ]



