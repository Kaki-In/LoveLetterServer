from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

import board_game as _board_game

class LoveLetterTurnRule(LoveLetterRule):
    def __init__(self, task: LoveLetterPlayTurnTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)
        
        self._player = task.get_effective_player()
        self._state = task.get_turn_state()
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        print("Executing start of Turn rule")
        return []
    
    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        print("Executing end of Turn rule")
        return []

    def should_be_played_again(self, context: LoveLetterGameContext) -> bool:
        return False
    
    def requires_players_interaction(self, context: LoveLetterGameContext) -> bool:
        return False
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        turn_state = self._state
        player = turn_state.get_player()

        return [
            LoveLetterDrawCardTask(player),
            LoveLetterChooseCardTask(player, turn_state),
            LoveLetterPlayChosenCardTask(player, turn_state)
        ]


