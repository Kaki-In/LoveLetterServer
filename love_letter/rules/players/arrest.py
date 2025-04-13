from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.actions import *

class LoveLetterArrestPlayerRule(LoveLetterRule[LoveLetterArrestPlayerTask]):
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        task = self.get_task()

        return [
            LoveLetterChoosePlayerTask(task.get_effective_player(), task.get_player_state(), LOVE_LETTER_CHOOSE_PLAYER_REASON.ARREST),
            LoveLetterChooseCharacterTask(task.get_effective_player(), task.get_character_state(), LOVE_LETTER_CHOOSE_CHARACTER_REASON.ARREST),
        ]

    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        task = self.get_task()

        if not task.get_character_state().has_chosen_character():
            return []
        
        player = task.get_player_state().get_chosen_player()
        character = task.get_character_state().get_chosen_character()

        if player.get_card().get_character() == character:
            player.eliminate()

            return [
                LoveLetterArrestPlayerAction(task.get_effective_player(), player, character)
            ]

        else:
            return [
                LoveLetterArrestPlayerFailedAction(task.get_effective_player(), player, character)
            ]


