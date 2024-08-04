from .task import *

from ...objects.context.board import *

class LoveLetterChooseCardTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__()
        self._effective_player = player

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._effective_player

