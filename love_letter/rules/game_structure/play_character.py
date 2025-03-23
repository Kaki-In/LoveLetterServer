from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.enum import *
from love_letter.mapping.character_tasks_map import *

class LoveLetterPlayCharacterRule(LoveLetterRule):
    def __init__(self, task: LoveLetterPlayCharacterTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)

        self._player = task.get_effective_player()
        self._character = task.get_character()

        self._characters_map = LoveLetterCharacterTasksMap()
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        task = self._characters_map.get_task(self._character, context.get_board(), context.get_configuration(), player = self._player)

        return [
            task
        ]

