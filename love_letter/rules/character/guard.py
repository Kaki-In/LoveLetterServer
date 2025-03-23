from love_letter.actions import *

from .character import *

class LoveLetterPlayGuardCharacterRule(LoveLetterCharacterRule[LoveLetterPlayGuardCharacterTask]):
    def __init__(self, task: LoveLetterPlayGuardCharacterTask, criteria: LoveLetterCriteria):
        LoveLetterCharacterRule.__init__(self, task, criteria)

        self._player = task.get_effective_player()
        self._state = task.get_state()
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
#        turn_state = context.get_state().get_round_state().get_turn_state()
#        turn_state.set_character_state(LoveLetterGuardCharacterState(self._player))
        return []

    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return [
            LoveLetterArrestPlayerTask(self._player, self._state, self._state)
        ]
    

