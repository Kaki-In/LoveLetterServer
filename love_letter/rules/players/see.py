from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.actions import *

class LoveLetterSeePlayerRule(LoveLetterRule[LoveLetterSeePlayerTask]):
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        task = self.get_task()
        effective_player = task.get_effective_player()

        return [
            LoveLetterChoosePlayerTask(effective_player, task.get_player_state(), LOVE_LETTER_CHOOSE_PLAYER_REASON.LOOK_AT),
            LoveLetterShowPlayerCardTask(effective_player, self.nothing, LOVE_LETTER_CHOOSE_CHARACTER_REASON.ARREST),
        ]

    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        return []


