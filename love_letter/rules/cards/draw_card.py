from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.actions import *

class LoveLetterDrawCardRule(LoveLetterRule):
    def __init__(self, task: LoveLetterDrawCardTask):
        super().__init__(task)

        self._player = task.get_player()

    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        deck = context.get_board().get_deck()

        card = deck.take_card()
        self._player.take_card(card)

        return [LoveLetterDrawCardAction(self._player, card)]
    
