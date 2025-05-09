from love_letter.base_struct.action import *
from love_letter.context import *

class LoveLetterDrawCardAction(LoveLetterAction):
    def __init__(self, player: LoveLetterPlayer, card: LoveLetterCard) -> None:
        LoveLetterAction.__init__(self)

        self._player = player
        self._card = card
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_card(self) -> LoveLetterCard:
        return self._card

