from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

import typing as _T

class LoveLetterDiscardRule(LoveLetterRule[LoveLetterDiscardTask]):
    def execute_start(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        task = self.get_task()
        player = task.get_effective_player()

        if task.get_card() == LOVE_LETTER_PLAYER_CARD.PLAYER_CARD:
            card = player.get_card()
            player.lay_card()
        else:
            card = player.get_drawn_card()
            player.lay_drawn_card()

        player.add_to_discard(card)

        return [
            LoveLetterDiscardAction(player, card, task.get_card(), task.get_reason())
        ]



