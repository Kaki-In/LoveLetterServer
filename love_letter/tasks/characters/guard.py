from .character import *
from love_letter.states import *

class LoveLetterPlayGuardCharacterTask(LoveLetterCharacterTask):
    def __init__(self, player: LoveLetterPlayer, context: LoveLetterContext):
        LoveLetterCharacterTask.__init__(self, player)

        players = context.get_board().get_available_players()
        other_players = []

        for available_player in players:
            if available_player is not player:
                other_players.append(available_player)
            
        characters = [
            i[0]
            for i in context.get_configuration().get_characters_configuration().get_characters()
            if i is not LOVE_LETTER_CHARACTER_GUARD
        ]

        self._state = LoveLetterGuardCharacterState(player, characters, other_players)

    def get_state(self) -> LoveLetterGuardCharacterState:
        return self._state

