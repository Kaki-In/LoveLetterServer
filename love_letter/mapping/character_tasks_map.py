from love_letter.tasks import *
from love_letter.base_struct.action import *
from love_letter.objects import *

import board_game as _board_game

class LoveLetterCharacterTasksMap(_board_game.BoardGameObjectTasksMap[LoveLetterCharacter, LoveLetterCharacterTask]):
    def __init__(self) :
        super().__init__()

        self.add_task(LOVE_LETTER_CHARACTER_GUARD, LoveLetterPlayGuardCharacterTask)

    def add_task(self, task: LoveLetterCharacter, rule: type[LoveLetterCharacterTask]) -> None:
        return super().add_task(task, rule)
    
    def get_task(self, object: LoveLetterCharacter, board: LoveLetterBoard, **args) -> LoveLetterCharacterTask:
        return super().get_task(object, board=board, **args)
    
    