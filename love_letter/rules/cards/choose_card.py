from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

import board_game as _board_game

class LoveLetterChooseCardRule(LoveLetterRule):
    def __init__(self, task: LoveLetterChooseCardTask):
        super().__init__(task)

        self._player = task.get_effective_player()
        self._state = task.get_needing_card_state()

    def requires_players_interaction(self, context: LoveLetterGameContext) -> bool:
        return not self._state.has_chosen_player()
    
    def get_interaction_subject(self, context: LoveLetterGameContext) -> _board_game.BoardGameClientInteraction:
        return LoveLetterChooseCardInteraction(self._player)
    
    def execute_response(self, context: LoveLetterGameContext, response: LoveLetterChooseCardResponse) -> list[LoveLetterAction]:
        card = response.get_card()

        self._state.set_chosen_player_card(card)

        return []
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return []

