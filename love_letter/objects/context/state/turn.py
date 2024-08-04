from .character import *

from ..board import *
from ....enum import *

import typing as _T

class LoveLetterTurnState():
    def __init__(self, player: LoveLetterPlayer):
        self._player = player

        self._chosen_card: _T.Optional[LOVE_LETTER_PLAYER_CARD] = None
        self._character: _T.Optional[LoveLetterCharacter] = None
        self._char_state: _T.Optional[LoveLetterCharacterState] = None
    
    def get_player(self) -> LoveLetterPlayer:
        return self._player
    
    def has_chosen_card(self) -> bool:
        return self._chosen_card is not None and self._char_state is not None
    
    def get_chosen_card(self) -> LOVE_LETTER_PLAYER_CARD:
        if self._chosen_card is None:
            raise ValueError('the player did not choose a character to play yet')
        
        return self._chosen_card
    
    def get_character_state(self) -> LoveLetterCharacterState:
        if self._char_state is None:
            raise ValueError('the player did not choose a character to play yet')
        
        return self._char_state
    
    def get_character(self) -> LoveLetterCharacter:
        if self._character is None:
            raise ValueError("the player did not choose a character to play yet")
        
        return self._character
    
    def set_chosen_card (self, card: LOVE_LETTER_PLAYER_CARD, character: LoveLetterCharacter, state: LoveLetterCharacterState) -> None:
        if self.has_chosen_card():
            raise ValueError('the player already chose a character')
        
        self._char_state = state
        self._chosen_card = card
        self._character = character

