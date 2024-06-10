from .card import *
from .character import *
import random as _random

import events as _events

DECK_EVENT_TOOK = 0

class LoveLetterDeck():
    def __init__(self):
        self._cards: list[ LoveLetterCard ] = []
        
        cards = []
        for _ in range(5):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_GUARD))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_PRIEST))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_BARON))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_HANDMAID))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_PRINCE))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_KING))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_COUNTESS))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LOVE_LETTER_CHARACTER_PRINCESS))
        
        for _ in range(16):
            card = cards.pop( _random.randrange(len(cards)) )
            self._cards.append( card )
        
        self._events = _events.EventObject(
            DECK_EVENT_TOOK
        )
        
    
    def takeCard(self) -> LoveLetterCard:
        card = self._cards.pop()
        self._events[ DECK_EVENT_TOOK ].emit(card)
        return card
    
    def __len__(self) -> int:
        return len(self._cards)
