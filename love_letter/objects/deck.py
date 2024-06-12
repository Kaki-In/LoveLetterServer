from .card import *
from .character import *

import random as _random
import events as _events

DECK_EVENT_TOOK = 0

class LoveLetterDeck():
    def __init__(self):
        self._cards: list[ LoveLetterCard ] = []
    
    def add_card(self, card):
        self._cards.append(card)
    
    def shuffle(self):
        _random.shuffle(self._cards)
    
    def take_card(self) -> LoveLetterCard:
        card = self._cards.pop()

#        self._events[ DECK_EVENT_TOOK ].emit(card)

        return card
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def toJson(self):
        return {
            'cards': [card.toJson() for card in self._cards]
        }
    
