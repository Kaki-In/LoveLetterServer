from .characters import *

class LoveLetterCard():
    def __init__(self, character: LoveLetterCharacter):
        self._character: LoveLetterCharacter = character
        
    def getCharacter(self) -> LoveLetterCharacter:
        return self._character
    
    def __lt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.getCharacter() < second_card.getCharacter()
    
    def __gt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.getCharacter() > second_card.getCharacter()
    
    def __eq__(self, second_card: 'LoveLetterCard') -> bool:
        return self.getCharacter() == second_card.getCharacter()
    
