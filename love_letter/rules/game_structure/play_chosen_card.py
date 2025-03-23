from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.enum import *

class LoveLetterPlayChosenCardRule(LoveLetterRule):
    def __init__(self, task: LoveLetterPlayChosenCardTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)

        self._player = task.get_player()
        self._card_state = task.get_chosen_card_state()

    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        card = self._card_state.get_chosen_player_card()
        
        if card == LOVE_LETTER_PLAYER_CARD.PLAYER_CARD:
            player_card = self._player.get_card()
        else:
            player_card = self._player.get_drawn_card()

        return [
            LoveLetterDiscardTask(self._player, LOVE_LETTER_DISCARD_REASON.PLAY, card),
            LoveLetterPlayCharacterTask(self._player, player_card.get_character())
        ]

