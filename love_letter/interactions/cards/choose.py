from love_letter.base_struct.interaction import *
from love_letter.board import *

class LoveLetterChooseCardInteraction(LoveLetterClientInteraction):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__('cards.choose', {
            'player': player.get_id()
        })

        self._player = player
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player

