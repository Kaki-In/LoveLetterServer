import typing as _T

from love_letter.base_struct.interaction import *
from love_letter.context import *
from love_letter.response import *
from love_letter.tasks import *

class LoveLetterChooseCardInteraction(LoveLetterClientInteraction[LoveLetterChooseCardResponse, LoveLetterChooseCardTask]):
    def toJson(self):
        return {
            'player': self.get_task().get_effective_player().get_id()
        }
    
    def json_to_response(self, json_data, context: LoveLetterContext) -> LoveLetterChooseCardResponse:
        if json_data == "HAND_CARD":
            return LoveLetterChooseCardResponse(LOVE_LETTER_PLAYER_CARD.PLAYER_CARD)
        elif json_data == "DRAWN_CARD":
            return LoveLetterChooseCardResponse(LOVE_LETTER_PLAYER_CARD.PLAYER_DRAWN_CARD)
        else:
            raise ValueError("invalid json response data")
    

