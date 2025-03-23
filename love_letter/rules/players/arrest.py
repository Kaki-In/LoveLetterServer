from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.actions import *

class LoveLetterArrestPlayerRule(LoveLetterRule):
    def __init__(self, task: LoveLetterArrestPlayerTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)

        self._player = task.get_effective_player()
        self._player_state = task.get_player_state()
        self._character_state = task.get_character_state()
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return [
            LoveLetterChoosePlayerTask(self._player, self._player_state, LOVE_LETTER_CHOOSE_PLAYER_REASON.ARREST),
            LoveLetterChooseCharacterTask(self._player, self._character_state, LOVE_LETTER_CHOOSE_CHARACTER_REASON.ARREST),
        ]

    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        if not self._character_state.has_chosen_character():
            return []
        
        player = self._player_state.get_chosen_player()
        character = self._character_state.get_chosen_character()

        if player.get_card().get_character() == character:
            player.eliminate()

            return [
                LoveLetterArrestPlayerAction(self._player, player, character)
            ]

        else:
            return [
                LoveLetterArrestPlayerFailedAction(self._player, player, character)
            ]


