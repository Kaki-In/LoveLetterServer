from .character import *

from love_letter.base_struct.states import *
from love_letter.context import *
from love_letter.configuration import *

import typing as _T

class LoveLetterGuardCharacterState(LoveLetterNeedingCharacterState, LoveLetterNeedingPlayerState):
    def __init__(self, player: LoveLetterPlayer, characters: list[LoveLetterCharacter], other_players: list[LoveLetterPlayer]):
        LoveLetterNeedingCharacterState.__init__(self, characters)
        LoveLetterNeedingPlayerState.__init__(self, other_players)

        self._effective_player = player

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._effective_player
