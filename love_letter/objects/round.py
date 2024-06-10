from .player import *
from .deck import *

class LoveLetterRound():
    def __init__(self, players: tuple[LoveLetterPlayer, ...], player_turn: int):
        self._players: tuple[LoveLetterPlayer, ...] = players
        self._deck: LoveLetterDeck = LoveLetterDeck()
        self._player_turn: int = player_turn
        
        self._hidden_card: LoveLetterCard | None = self._deck.takeCard()
        self._remove_cards: list[LoveLetterCard] = list()
        
        if len(players) == 2:
            for _ in range(3):
                self._remove_cards.append(self._deck.takeCard())
    
    def getPlayers(self) -> tuple[LoveLetterPlayer, ...]:
        return self._players
    
    def getDeck(self) -> LoveLetterDeck:
        return self._deck
    
    def getActivePlayer(self) -> LoveLetterPlayer:
        return self._players[ self._player_turn ]
    
    def getAvailablePlayers(self) -> tuple[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not (player.is_eliminated() or player.is_protected()):
                players.append(player)
        
        return tuple(players)
    
    def getAlivePlayers(self) -> tuple[LoveLetterPlayer]:
        players = []
        for player in self._players:
            if not player.is_eliminated():
                players.append(player)
        
        return tuple(players)
    
    def getHiddenCard(self) -> LoveLetterCard | None:
        return self._hidden_card
    
    def getRemovedCards(self) -> tuple[LoveLetterCard, ...]:
        return tuple(self._remove_cards)    
