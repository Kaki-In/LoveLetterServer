from .player import *
from .round import *

import random as _random
import events as _events

GAME_EVENT_INITIALIZATION   = 0
GAME_EVENT_NEW_ROUND        = 1
GAME_EVENT_RESULTS          = 2

class LoveLetterGame():
    def __init__(self, *players: LoveLetterPlayer):
        self._players: tuple[LoveLetterPlayer, ...] = players
        
        self._round: LoveLetterRound | None = None
        
        self._events = _events.EventObject(
            GAME_EVENT_NEW_ROUND,
            GAME_EVENT_INITIALIZATION,
            GAME_EVENT_RESULTS
        )
    
    def players(self):
        return self._players
    
    def get_actual_round(self):
        return self._round
    
    def get_events(self):
        return self._events
    
    def init_new_round(self):
        self._round = LoveLetterRound(self._players, _random.randrange(len(self._players)))
        
        self._events[ GAME_EVENT_INITIALIZATION ].emit()
