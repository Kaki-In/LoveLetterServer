from ..board import *

class LoveLetterCharactersConfiguration():
    def __init__(self, *characters: LoveLetterCharacter):
        self._characters = characters

    def get_characters(self) -> tuple[LoveLetterCharacter, ...]:
        return self._characters

LOVE_LETTER_CHARACTER_CONFIGURATION_DEFAULT = LoveLetterCharactersConfiguration(
    LOVE_LETTER_CHARACTER_GUARD,
    LOVE_LETTER_CHARACTER_PRIEST,
    LOVE_LETTER_CHARACTER_BARON,
    LOVE_LETTER_CHARACTER_HANDMAID,
    LOVE_LETTER_CHARACTER_PRINCE,
    LOVE_LETTER_CHARACTER_KING,
    LOVE_LETTER_CHARACTER_COUNTESS,
    LOVE_LETTER_CHARACTER_PRINCESS
)

