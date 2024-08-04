from .result import *

from ...objects.context.board import *

class LoveLetterRoundResult(LoveLetterResult):
    def __init__(self, winners: list[LoveLetterPlayer]):
        super().__init__()

        self._winners = winners
    
    def get_winners(self) -> list[LoveLetterPlayer]:
        return self._winners
    
