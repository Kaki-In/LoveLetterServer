from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

class LoveLetterChoosePlayerRule(LoveLetterRule):
    def __init__(self, task: LoveLetterChoosePlayerTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)

        self._player = task.get_effective_player()
        self._player_state = task.get_chosen_player_state()
        self._reason = task.get_reason()

    def requires_players_interaction(self, context: LoveLetterGameContext) -> bool:
        return not self._player_state.has_chosen_player()
    
    def get_interaction_subject(self, context: LoveLetterGameContext) -> LoveLetterChoosePlayerInteraction:
        return LoveLetterChoosePlayerInteraction(context.get_board(), LoveLetterChoosePlayerTask(
            self._player,
            self._player_state,
            self._reason
        ))
    
    def execute_response(self, context: LoveLetterGameContext, response: LoveLetterChoosePlayerResponse) -> list[LoveLetterAction]:
        player = response.get_player()

        self._player_state.set_chosen_player(player)

        return []
    

