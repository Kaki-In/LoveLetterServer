from love_letter.base_struct.rule import *
from love_letter.tasks import *

class LoveLetterCharacterRule(LoveLetterRule):
    def __init__(self, task: LoveLetterCharacterTask):
        super().__init__(task)

        self._player = task.get_effective_player()
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
