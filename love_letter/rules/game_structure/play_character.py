from love_letter.base_struct.rule import *
from love_letter.tasks import *
from love_letter.enum import *
from love_letter.mapping.character_tasks_map import *

class LoveLetterPlayCharacterRule(LoveLetterRule[LoveLetterPlayCharacterTask]):
    def __init__(self, task: LoveLetterPlayCharacterTask):
        LoveLetterRule.__init__(self, task)

        self._characters_map = LoveLetterCharacterTasksMap()
    
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        task = self._characters_map.get_task(self.get_task().get_character(), player = self.get_task().get_effective_player(), context = context)

        return [
            task
        ]

