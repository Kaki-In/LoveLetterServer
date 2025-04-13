from love_letter.configuration import *
from love_letter.context import *

from .round import *

import typing as _T

class LoveLetterGameState():
    def __init__(self, configuration: LoveLetterConfiguration, board: LoveLetterBoard):
        self._configuration = configuration
        self._board = board
        self._actual_round: _T.Optional[LoveLetterRoundState] = None
    
    def get_actual_round(self) -> LoveLetterRoundState:
        if self._actual_round is None:
            raise ValueError("no round defined yet")
        
        return self._actual_round
    
    def has_round_defined(self) -> bool:
        return self._actual_round is not None
    
    def set_actual_round(self, round: LoveLetterRoundState) -> None:
        self._actual_round = round
    
    def get_configuration(self) -> LoveLetterConfiguration:
        return self._configuration
    
    def get_board(self) -> LoveLetterBoard:
        return self._board
        
    def get_winners(self) -> list[LoveLetterPlayer]:
        max_rounds_count = self.get_max_rounds_count()

        players = []

        for player in self._board.get_players():
            if player.get_won_rounds() >= max_rounds_count:
                players.append(player)
        
        return players
    
    def get_max_rounds_count(self) -> int:
        game_configuration = self._configuration.get_game_configuration()

        if game_configuration.has_max_rounds_imposed():
            return game_configuration.get_max_rounds()
        
        players_count = len(self._board.get_players())

        if   players_count == 2:
            return 7
        
        elif players_count == 3:
            return 5
        
        elif players_count == 4:
            return 4
        
        raise ReferenceError('there is no default rounds count for this number of players')

