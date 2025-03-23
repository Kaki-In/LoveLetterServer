from .character import *
from love_letter.states import *

class LoveLetterPlayGuardCharacterTask(LoveLetterCharacterTask):
    def __init__(self, player: LoveLetterPlayer, board: LoveLetterBoard, configuration: LoveLetterConfiguration):
        LoveLetterCharacterTask.__init__(self, player, board, configuration)

        self._state = LoveLetterGuardCharacterState(player, board, configuration)

    def get_state(self) -> LoveLetterGuardCharacterState:
        return self._state

