import typing as _T

from love_letter.base_struct.interaction import *
from love_letter.board import *
from love_letter.response import *
from love_letter.tasks import *

class LoveLetterChooseCharacterInteraction(LoveLetterClientInteraction[LoveLetterChooseCharacterResponse, LoveLetterChooseCharacterTask]):
    def get_player(self) -> LoveLetterPlayer:
        return self.get_task().get_effective_player()
    
    def toJson(self):
        state = self.get_task().get_chosen_character_state()

        possibilities = state.get_chosable_characters()

        return {
            'player': self.get_task().get_effective_player().toJson(),
            'possibilities': [
                i.get_name() for i in possibilities
            ]
        }
    
    def json_to_response(self, json_data) -> LoveLetterChooseCharacterResponse:
        raise NotImplementedError()
    

