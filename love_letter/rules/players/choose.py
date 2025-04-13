from love_letter.base_struct.interactive_rule import *
from love_letter.tasks import *
from love_letter.interactions import *
from love_letter.response import *

class LoveLetterChoosePlayerRule(LoveLetterInteractiveRule[LoveLetterChoosePlayerTask, LoveLetterChoosePlayerResponse, LoveLetterChoosePlayerInteraction]):
    def requires_players_interaction(self, context: LoveLetterContext) -> bool:
        return not self.get_task().get_chosen_player_state().has_chosen_player()
    
    def get_interaction_subject(self, context: LoveLetterContext) -> LoveLetterChoosePlayerInteraction:
        task = self.get_task()

        return LoveLetterChoosePlayerInteraction(LoveLetterChoosePlayerTask(
            task.get_effective_player(),
            task.get_chosen_player_state(),
            task.get_reason()
        ))
    
    def execute_response(self, response: LoveLetterChoosePlayerResponse, context: LoveLetterContext) -> list[LoveLetterAction]:
        player = response.get_player()

        self.get_task().get_chosen_player_state().set_chosen_player(player)

        return []
    

