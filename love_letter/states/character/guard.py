from .character import *
from love_letter.board import *

import typing as _T

class LoveLetterGuardCharacterState(LoveLetterCharacterState, ):
    def __init__(self, player: LoveLetterPlayer):
        super().__init__()

        self._chosen_player: _T.Optional[LoveLetterPlayer] = None
        self._effective_player = player
        self._chosen_character: _T.Optional[LoveLetterCharacter] = None
    
    def get_effective_player(self) -> LoveLetterPlayer:
        return self._effective_player
    
    def has_chosen_player(self) -> bool:
        return self._chosen_player is not None
    
    def get_chosen_player(self) -> LoveLetterPlayer:
        if self._chosen_player is None:
            raise TypeError("the player has not been chosen yet")
        
        return self._chosen_player
    
    def get_chosen_character(self) -> LoveLetterCharacter:
        if self._chosen_character is None:
            raise ValueError("no character has been chosen yet")
        
        return self._chosen_character
    
    def has_chosen_character(self) -> bool:
        return self._chosen_character is not None
    
    def set_chosen_character(self, character: LoveLetterCharacter) -> None:
        self._chosen_character = character


