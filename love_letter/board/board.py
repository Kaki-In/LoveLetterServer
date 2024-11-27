from .player import *
from .deck import *

import typing as _T

import board_game as _board_game

class LoveLetterBoard(_board_game.BoardGameBoard):
    def __init__(self, players: list[LoveLetterPlayer], deck: LoveLetterDeck):
        super().__init__()
        self._players = players.copy()
        self._deck: LoveLetterDeck = deck
    
    def get_players(self) -> list[LoveLetterPlayer]:
        return self._players.copy()
    
    def get_available_players(self) -> list[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not (player.is_eliminated() or player.is_protected()):
                players.append(player)
        
        return players
    
    def get_alive_players(self) -> list[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not player.is_eliminated():
                players.append(player)
        
        return players
    
    def get_player_by_id(self, id: int) -> LoveLetterPlayer:
        for player in self._players:
            if player.get_id() == id:
                return player
        
        raise KeyError('no such player')
    
    def get_deck(self) -> LoveLetterDeck:
        return self._deck
    
    def toJson(self):
        return {
            'players': [player.toJson() for player in self._players],
            'deck': self._deck.toJson()
        }
    

