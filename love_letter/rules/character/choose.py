from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

import board_game as _board_game

class LoveLetterChooseCharacterRule(LoveLetterRule[LoveLetterChooseCharacterTask]):
    def requires_players_interaction(self) -> bool:
        return not self.get_task().get_state().has_chosen_character()
    
    def get_interaction_subject(self) -> _board_game.BoardGameClientInteraction:
        return LoveLetterChooseCharacterInteraction(
            self.get_task()
        )
    
    def execute_response(self, response: LoveLetterChooseCharacterResponse) -> list[LoveLetterAction]:
        character = response.get_character()

        self.get_task().get_state().set_chosen_character(character)

        return []
    
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        return []

