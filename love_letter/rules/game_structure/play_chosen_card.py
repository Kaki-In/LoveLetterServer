from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.enum import *

class LoveLetterPlayChosenCardRule(LoveLetterRule[LoveLetterPlayChosenCardTask]):
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        task = self.get_task()
        player = task.get_player()
        
        card = task.get_chosen_card_state().get_chosen_player_card()
        
        if card == LOVE_LETTER_PLAYER_CARD.PLAYER_CARD:
            player_card = player.get_card()
        else:
            player_card = player.get_drawn_card()

        return [
            LoveLetterDiscardTask(player, LOVE_LETTER_DISCARD_REASON.PLAY, card),
            LoveLetterPlayCharacterTask(player, player_card.get_character())
        ]

