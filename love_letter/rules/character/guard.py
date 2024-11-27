from love_letter.actions import *

from .character import *
from .guard_steps import *

class LoveLetterPlayGuardCharacterRule(LoveLetterCharacterRule):
    def __init__(self, task: LoveLetterPlayGuardCharacterTask):
        super().__init__(task)

        self._player = task.get_effective_player()
        self._player_state = task.get_chosen_player_state()
        self._character_state = task.get_chosen_character_state()
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
#        turn_state = context.get_state().get_round_state().get_turn_state()
#        turn_state.set_character_state(LoveLetterGuardCharacterState(self._player))

        return []

    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return [
            LoveLetterArrestPlayerTask(self._player, self._player_state, self._character_state)
        ]


