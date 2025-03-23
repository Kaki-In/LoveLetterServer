from love_letter.base_struct.action import *
from love_letter.objects import *

class LoveLetterEndGameAction(LoveLetterAction):
    def __init__(self, winners: list[LoveLetterPlayer]):
        LoveLetterAction.__init__(self)

        self._winners = winners
    
    def get_winners(self) -> list[LoveLetterPlayer]:
        return self._winners


