from .player import *
from .deck import *

import typing as _T

class LoveLetterRound():
    def __init__(self, players: tuple[LoveLetterPlayer, ...], player_turn: int, deck: LoveLetterDeck):
        self._players: tuple[LoveLetterPlayer, ...] = players
        self._deck = deck
        self._player_turn: int = player_turn
        
        self._hidden_card: LoveLetterCard | None = self._deck.takeCard()
        self._remove_cards: list[LoveLetterCard] = list()
        
        if len(players) == 2:
            for _ in range(3):
                self._remove_cards.append(self._deck.takeCard())
    
    def get_players(self) -> tuple[LoveLetterPlayer, ...]:
        return self._players
    
    def get_deck(self) -> LoveLetterDeck:
        return self._deck
    
    def get_active_player(self) -> LoveLetterPlayer:
        return self._players[ self._player_turn ]
    
    def get_available_players(self) -> tuple[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not (player.is_eliminated() or player.is_protected()):
                players.append(player)
        
        return tuple(players)
    
    def get_alive_players(self) -> tuple[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not player.is_eliminated():
                players.append(player)
        
        return tuple(players)
    
    def get_hidden_cards(self) -> LoveLetterCard | None:
        return self._hidden_card
    
    def get_removed_cards(self) -> tuple[LoveLetterCard, ...]:
        return tuple(self._remove_cards)
    
    def get_player_by_id(self, id: int) -> LoveLetterPlayer:
        for player in self._players:
            if player.get_id() == id:
                return player
    
    def draw(self) -> LoveLetterCard:
        if len(self._deck):
            return self._deck.take_card()
        
        return self._hidden_card
    
    def select_next_player(self):
        while True:
            self._player_turn = ( self._player_turn + 1 ) % len(self._players)
            
    

