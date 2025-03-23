from love_letter.board import *

class LoveLetterCharactersConfiguration():
    def __init__(self, *characters: tuple[LoveLetterCharacter, int]):
        self._characters = [i[:2] for i in characters]

    def get_characters(self) -> list[tuple[LoveLetterCharacter, int]]:
        return self._characters.copy()

LOVE_LETTER_CHARACTER_CONFIGURATION_DEFAULT = LoveLetterCharactersConfiguration(
    (LOVE_LETTER_CHARACTER_GUARD, 5),
#    (LOVE_LETTER_CHARACTER_PRIEST, 2),
#    (LOVE_LETTER_CHARACTER_BARON, 2),
#    (LOVE_LETTER_CHARACTER_HANDMAID, 2),
#    (LOVE_LETTER_CHARACTER_PRINCE, 2),
#    (LOVE_LETTER_CHARACTER_KING, 1),
#    (LOVE_LETTER_CHARACTER_COUNTESS, 1),
#    (LOVE_LETTER_CHARACTER_PRINCESS, 1)
)

