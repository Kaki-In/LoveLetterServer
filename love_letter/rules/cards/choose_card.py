from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

import board_game as _board_game

class LoveLetterChooseCardRule(LoveLetterRule[LoveLetterChooseCardTask]):
    def requires_players_interaction(self, context: LoveLetterGameContext) -> bool:
        return not self.get_task().get_needing_card_state().has_chosen_player()
    
    def get_interaction_subject(self, context: LoveLetterGameContext) -> _board_game.BoardGameClientInteraction:
        return LoveLetterChooseCardInteraction(context.get_board(), self.get_task())
    
    def execute_response(self, context: LoveLetterGameContext, response: LoveLetterChooseCardResponse) -> list[LoveLetterAction]:
        card = response.get_card()

        self.get_task().get_needing_card_state().set_chosen_player_card(card)

        return []
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return []

