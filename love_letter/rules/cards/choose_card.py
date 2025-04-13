from love_letter.base_struct.rule import *
from love_letter.base_struct.interactive_rule import *
from love_letter.actions import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

import board_game as _board_game

class LoveLetterChooseCardRule(LoveLetterInteractiveRule[LoveLetterChooseCardTask, LoveLetterChooseCardResponse, LoveLetterChooseCardInteraction]):
    def requires_players_interaction(self, context: LoveLetterContext) -> bool:
        return not self.get_task().get_state().has_chosen_player()
    
    def get_interaction_subject(self, context: LoveLetterContext) -> LoveLetterChooseCardInteraction:
        return LoveLetterChooseCardInteraction(self.get_task())
    
    def execute_response(self, response: LoveLetterChooseCardResponse, context: LoveLetterContext) -> list[LoveLetterAction]:
        card = response.get_card()

        self.get_task().get_state().set_chosen_player_card(card)

        return []
    
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        super().get_task
        return []
        

