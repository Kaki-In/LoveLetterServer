import typing as _T

from love_letter.base_struct.interaction import *
from love_letter.board import *
from love_letter.response import *
from love_letter.tasks import *

class LoveLetterChooseCardInteraction(LoveLetterClientInteraction[LoveLetterChooseCardResponse, LoveLetterChooseCardTask]):
    def get_player(self) -> LoveLetterPlayer:
        return self.get_task().get_effective_player()
    
    def toJson(self):
        return {
            'player': self.get_task().get_effective_player().toJson()
        }
    
    def json_to_response(self, json_data) -> LoveLetterChooseCardResponse:
        if json_data == "HAND_CARD":
            return LoveLetterChooseCardResponse(LOVE_LETTER_PLAYER_CARD.PLAYER_CARD)
        elif json_data == "DRAWN_CARD":
            return LoveLetterChooseCardResponse(LOVE_LETTER_PLAYER_CARD.PLAYER_DRAWN_CARD)
        else:
            raise ValueError("invalid json response data")
    

