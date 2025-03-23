from love_letter.base_struct.response import *
from love_letter.enum import *
from love_letter.board import *
import typing as _T

class LoveLetterChoosePlayerResponse(LoveLetterClientResponse):
    def __init__(self, player: LoveLetterPlayer):
        LoveLetterClientResponse.__init__(self)

        self._player = player

    def get_player(self) -> LoveLetterPlayer:
        return self._player
    
    def json_is_valid(json_data: _T.Any, board: LoveLetterBoard) -> bool:
        return type(json_data) is int and json_data in board.get_available_players()
    
    def fromJson(data: _T.Any, board: LoveLetterBoard) -> 'LoveLetterChoosePlayerResponse':
        player = board.get_player_by_id(data['id'])
        
        return LoveLetterChoosePlayerResponse(player)

