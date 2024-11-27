from love_letter.base_struct.response import *
from love_letter.enum import *
from love_letter.board import *

class LoveLetterChoosePlayerResponse(LoveLetterClientResponse):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__('players.choose', {
            'player': player
        })

        self._player = player

    def get_player(self) -> LoveLetterPlayer:
        return self._player

