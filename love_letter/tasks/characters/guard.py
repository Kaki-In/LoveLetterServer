from .character import *

class LoveLetterPlayGuardCharacterTask(LoveLetterCharacterTask):
    def __init__(self, player: LoveLetterPlayer, board: LoveLetterBoard):
        super().__init__(player)

        players = board.get_available_players()
        other_players = []

        for available_player in other_players:
            if available_player is not player:
                other_players.append(available_player)

        self._player_state = LoveLetterNeedingPlayerState(
            other_players
        )
        self._character_state = LoveLetterNeedingCharacterState(
            [
                LOVE_LETTER_CHARACTER_PRIEST,
                LOVE_LETTER_CHARACTER_BARON,
                LOVE_LETTER_CHARACTER_HANDMAID,
                LOVE_LETTER_CHARACTER_PRINCE,
                LOVE_LETTER_CHARACTER_KING,
                LOVE_LETTER_CHARACTER_COUNTESS,
                LOVE_LETTER_CHARACTER_PRINCESS
            ]
        )

    def get_chosen_player_state(self) -> LoveLetterNeedingPlayerState:
        return self._player_state
    
    def get_chosen_character_state(self) -> LoveLetterNeedingCharacterState:
        return self._character_state

