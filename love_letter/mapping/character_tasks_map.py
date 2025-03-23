from love_letter.tasks import *
from love_letter.base_struct.action import *
from love_letter.objects import *

import board_game as _board_game

class LoveLetterCharacterTasksMap(_board_game.BoardGameObjectTasksMap[LoveLetterCharacter, LoveLetterCharacterTask]):
    def __init__(self) :
        _board_game.BoardGameObjectTasksMap.__init__(self)

        self.add_task(LOVE_LETTER_CHARACTER_GUARD, LoveLetterPlayGuardCharacterTask)
        self._tasks_states = {}

    def add_task(self, task: LoveLetterCharacter, rule: type[LoveLetterCharacterTask]) -> None:
        return _board_game.BoardGameObjectTasksMap.add_task(self, task, rule)
    
    def get_task(self, object: LoveLetterCharacter, board: LoveLetterBoard, configuration: LoveLetterConfiguration, **args) -> LoveLetterCharacterTask:
        return _board_game.BoardGameObjectTasksMap.get_task(self, object, board=board, configuration=configuration, **args)
    
    