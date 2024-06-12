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
    
    def add_ghost(self, ghost: Client) -> None:
        self._ghosts.append(ghost)
    
    def remove_ghost(self, ghost: Client) -> None:
        self._ghosts.remove(ghost)
    
    def set_ghost_as_player(self, ghost: Client) -> None:
        if not ghost in self._ghosts:
            raise ReferenceError("no such ghost")
        
        self._ghosts.remove(ghost)
        self._players.append(ghost)
    
    def set_player_as_ghost(self, player: Client) -> None:
        if not player in self._players:
            raise ReferenceError("no such ghost")
        
        self._players.remove(player)
        self._ghosts.append(player)
    
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
    
    def toJson(self):
        game_json = None
        
        if self._game is not None:
            game_json = self._game.toJson()
        
        return {
            'state': self._state,
            'game': game_json,
            'ghosts_number': len(self._ghosts),
            'players': [player.toJson() for player in self._players]
        }
    
