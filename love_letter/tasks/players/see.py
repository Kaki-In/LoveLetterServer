from love_letter.base_struct.task import *
from love_letter.states import *

class LoveLetterSeePlayerTask(LoveLetterTask):
    def __init__(self, player: LoveLetterPlayer, player_state: LoveLetterNeedingPlayerState):
        LoveLetterTask.__init__(self)

        self._player = player
        self._player_state = player_state

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_player_state(self) -> LoveLetterNeedingPlayerState:
        return self._player_state


