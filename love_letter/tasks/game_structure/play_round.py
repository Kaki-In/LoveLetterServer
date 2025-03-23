from love_letter.base_struct.task import *
from love_letter.states import *

class LoveLetterPlayRoundTask(LoveLetterTask):
    def __init__(self, round_state: LoveLetterRoundState):
        LoveLetterTask.__init__(self)

        self._round_state = round_state

    def get_round_state(self) -> LoveLetterRoundState:
        return self._round_state

