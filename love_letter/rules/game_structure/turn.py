from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

import board_game as _board_game

class LoveLetterTurnRule(LoveLetterRule[LoveLetterPlayTurnTask]):
    def execute_start(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        print("Executing start of Turn rule")
        return []
    
    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        print("Executing end of Turn rule")
        return []

    def should_be_played_again(self, context: LoveLetterContext) -> bool:
        return False
    
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        turn_state = self.get_task().get_turn_state()
        player = turn_state.get_player()

        return [
            LoveLetterDrawCardTask(player),
            LoveLetterChooseCardTask(player, turn_state),
            LoveLetterPlayChosenCardTask(player, turn_state)
        ]


