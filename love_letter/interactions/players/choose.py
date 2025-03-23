from love_letter.base_struct.interaction import *
from love_letter.board import *
from love_letter.enum import *
from love_letter.tasks import *
from love_letter.response import *

class LoveLetterChoosePlayerInteraction(LoveLetterClientInteraction[LoveLetterChoosePlayerResponse, LoveLetterChoosePlayerTask]):
    def toJson(self):
        return {
            'player': self.get_task().get_effective_player().toJson(),
            'reason': self.get_task().get_reason().value
        }
    
    def json_to_response(self, json_data) -> LoveLetterChoosePlayerResponse:
        return LoveLetterChoosePlayerResponse(
            self.get_board().get_player_by_id(json_data["player"])
        )
        

