from .character import *

from love_letter.base_struct.states import *
from love_letter.board import *
from love_letter.configuration import *

import typing as _T

class LoveLetterGuardCharacterState(LoveLetterNeedingCharacterState, LoveLetterNeedingPlayerState):
    def __init__(self, player: LoveLetterPlayer, board: LoveLetterBoard, configuration: LoveLetterConfiguration):
        players = board.get_available_players()
        other_players = []

        for available_player in players:
            if available_player is not player:
                other_players.append(available_player)
            
        characters = [
            i[0]
            for i in configuration.get_characters_configuration().get_characters()
            if i is not LOVE_LETTER_CHARACTER_GUARD
        ]

        LoveLetterNeedingCharacterState.__init__(self, characters)
        LoveLetterNeedingPlayerState.__init__(self, other_players)

        self._effective_player = player

    def get_effective_player(self) -> LoveLetterPlayer:
        return self._effective_player
