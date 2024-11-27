class LoveLetterCharacter():
    def __init__(self, value: int, name: str):
        self._name: str = name
        self._value: int = value
        
    def get_name(self) -> str:
        return self._name
    
    def get_value(self) -> int:
        return self._value
    
    def __lt__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() < second_character.get_value()

    def __gt__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() > second_character.get_value()

    def __eq__(self, second_character: 'LoveLetterCharacter') -> bool:
        return self.get_value() == second_character.get_value()
    
    def __hash__(self) -> int:
        return id(self)

LOVE_LETTER_CHARACTER_GUARD     = LoveLetterCharacter(1, "Garde"    )
LOVE_LETTER_CHARACTER_PRIEST    = LoveLetterCharacter(2, "Prêtre"   )
LOVE_LETTER_CHARACTER_BARON     = LoveLetterCharacter(3, "Baron"    )
LOVE_LETTER_CHARACTER_HANDMAID  = LoveLetterCharacter(4, "Servante" )
LOVE_LETTER_CHARACTER_PRINCE    = LoveLetterCharacter(5, "Prince"   )
LOVE_LETTER_CHARACTER_KING      = LoveLetterCharacter(6, "Roi"      )
LOVE_LETTER_CHARACTER_COUNTESS  = LoveLetterCharacter(7, "Comtesse" )
LOVE_LETTER_CHARACTER_PRINCESS  = LoveLetterCharacter(8, "Princesse")

