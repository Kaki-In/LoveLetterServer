from .characters import *
from .rounds import *
from .game import *

import typing as _T

import board_game as _board_game

class LoveLetterConfiguration(_board_game.BoardGameConfiguration):
    def __init__(self, characters_configuration: LoveLetterCharactersConfiguration, rounds_configuration: LoveLetterRoundsConfiguration, game_configuration: LoveLetterGameConfiguration):
        _board_game.BoardGameConfiguration.__init__(self)
        
        self._char_conf = characters_configuration
        self._rounds_conf = rounds_configuration
        self._game_conf = game_configuration
    
    def get_characters_configuration(self) -> LoveLetterCharactersConfiguration:
        return self._char_conf
    
    def get_rounds_configuration(self) -> LoveLetterRoundsConfiguration:
        return self._rounds_conf
    
    def get_game_configuration(self) -> LoveLetterGameConfiguration:
        return self._game_conf


