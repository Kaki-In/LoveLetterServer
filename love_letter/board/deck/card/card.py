from .character import *

class LoveLetterCard():
    def __init__(self, character: LoveLetterCharacter):
        self._character: LoveLetterCharacter = character
        
    def get_character(self) -> LoveLetterCharacter:
        return self._character
    
    def __lt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.get_character() < second_card.get_character()
    
    def __gt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.get_character() > second_card.get_character()
    
    def __eq__(self, second_card: object) -> bool:
        if isinstance(second_card, LoveLetterCard):
            return self.get_character() == second_card.get_character()
        
        else:
            return False
    
    def toJson(self):
        return {
            'character_name': self._character.get_name()
        }
