from .client import *

import love_letter as _love_letter
import typing as _T

TABLE_STATE_WAITING     = 0
TABLE_STATE_STARTING    = 1
TABLE_STATE_PLAYING     = 2
TABLE_STATE_GAVE_UP     = 3
TABLE_STATE_FINISHED    = 4

class Table():
    def __init__(self):
        self._state = TABLE_STATE_WAITING
        self._game: _T.Optional[_love_letter.LoveLetterGame] = None
        
        self._ghosts: list[Client] = []
        self._players: list[Client] = []
    
    def get_ghosts(self) -> list[Client]:
        return self._ghosts
    
    def get_players(self) -> list[Client]:
        return self._players
    
    def get_state(self) -> int:
        return self._state
    
    def set_state(self, state: int) -> None:
        self._state = state
    
    def get_game(self) -> _T.Optional[_love_letter.LoveLetterGame]:
        return self._game
    
    def set_game(self, game: _love_letter.LoveLetterGame) -> None:
        self._game = game
    
    
