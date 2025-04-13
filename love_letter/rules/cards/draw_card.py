from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.actions import *

class LoveLetterDrawCardRule(LoveLetterRule[LoveLetterDrawCardTask]):
    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        deck = context.get_board().get_deck()
        player = self.get_task().get_player()

        card = deck.take_card()
        player.take_card(card)

        return [LoveLetterDrawCardAction(player, card)]
    
