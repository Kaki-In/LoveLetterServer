from .client import *

import typing as _T

TABLE_STATE_WAITING     = 0
TABLE_STATE_STARTING    = 1
TABLE_STATE_PLAYING     = 2
TABLE_STATE_GAVE_UP     = 3
TABLE_STATE_FINISHED    = 4

#class Table():
#    def __init__(self):
#        self._state = TABLE_STATE_WAITING
#        self._game: _T.Optional[_love_letter_objects.LoveLetterTable] = None
#        
#        self._ghosts: list[Client] = []
#        self._players: list[Client] = []
#    
#    def add_ghost(self, ghost: Client) -> None:
#        print("ghost added")
#        self._ghosts.append(ghost)
#    
#    def remove_ghost(self, ghost: Client) -> None:
#        print("ghost removed")
#        self._ghosts.remove(ghost)
#    
#    def set_ghost_as_player(self, ghost: Client) -> None:
#        print("ghost changed to player")
#        if not ghost in self._ghosts:
#            raise ReferenceError("no such ghost")
#        
#        self._ghosts.remove(ghost)
#        self._players.append(ghost)
#    
#    def set_player_as_ghost(self, player: Client) -> None:
#        print("player changed to ghost")
#        if not player in self._players:
#            raise ReferenceError("no such ghost")
#        
#        self._players.remove(player)
#        self._ghosts.append(player)
#    
#    def get_ghosts(self) -> list[Client]:
#        return self._ghosts
#    
#    def get_players(self) -> list[Client]:
#        return self._players
#    
#    def get_state(self) -> int:
#        return self._state
#    
#    def set_state(self, state: int) -> None:
#        print("state changed to", state)
#        self._state = state
#    
#    def get_game(self) -> _T.Optional[_love_letter_objects.LoveLetterTable]:
#        return self._game
#    
#    def set_game(self, game: _love_letter_objects.LoveLetterTable) -> None:
#        self._game = game
#    
#    def toJson(self):
#        game_json = None
#        
#        if self._game is not None:
#            game_json = self._game.toJson()
#        
#        return {
#            'state': self._state,
#            'game': game_json,
#            'ghosts_number': len(self._ghosts),
#            'players': [player.toJson() for player in self._players]
#        }
#    
#