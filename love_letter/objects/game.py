from .player import *
from .round import *

import random as _random
import events as _events
import typing as _T

GAME_EVENT_INITIALIZATION   = 0
GAME_EVENT_NEW_ROUND        = 1
GAME_EVENT_RESULTS          = 2

class LoveLetterGame():
    def __init__(self, *players: LoveLetterPlayer):
        if len(players) < 2:
            raise ValueError("two players or more are required to play this game")
        
        self._players: tuple[LoveLetterPlayer, ...] = players
        
        self._round: _T.Optional[LoveLetterRound] = None
        
        self._events = _events.EventObject(
            GAME_EVENT_NEW_ROUND,
            GAME_EVENT_INITIALIZATION,
            GAME_EVENT_RESULTS
        )
    
    def get_players(self):
        return self._players
    
    def get_actual_round(self):
        return self._round
    
    def get_events(self):
        return self._events
    
    def init_new_round(self, deck: LoveLetterDeck):
        if self._round:
            actual_winner = _random.choice(self._round.get_winners())
        else:
            actual_winner = _random.choice(self._players)
        
        self._round = LoveLetterRound(self._players, self._players.index(actual_winner), deck)
        
        self._events[ GAME_EVENT_INITIALIZATION ].emit()
    
    def toJson(self):
        round_json = None
        
        if self._round is not None:
            round_json = self._round.toJson()
        
        return {
            'players': [player.toJson() for player in self._players],
            'round': round_json,
        }
    
