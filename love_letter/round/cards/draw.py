from .card import *
import random as _random

class LoveLetterDraw():
    def __init__(self):
        self._cards = []
        cards = []
        
        for _ in range(5):
            cards.append(LoveLetterCard(LoveLetterGuard))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LoveLetterPriest))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LoveLetterBaron))

        for _ in range(2):
            cards.append(LoveLetterCard(LoveLetterServant))
        
        for _ in range(2):
            cards.append(LoveLetterCard(LoveLetterPrince))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LoveLetterKing))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LoveLetterCountess))
        
        for _ in range(1):
            cards.append(LoveLetterCard(LoveLetterPrincess))
        
        for _ in range(16):
            card = cards.pop( _random.randrange(len(cards)) )
            self._cards.append(card)
    
    def takeCard(self):
        return self._cards.pop()
    
    def __len__(self):
        return len(self._cards)
