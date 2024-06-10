from ..mapping import *
from ..objects import *

from .player_turn import *
from .character import *

import typing as _T

class LoveLetterRoundRule():
    def __init__(self):
        self._players_rule = LoveLetterPlayerTurnRule()
    
    async def main_round(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        while not self.is_finished():
            await self._players_rule.play(mapper, notifier, round)
            round.select_next_player()
    
    async def make_player_discard(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, player: LoveLetterPlayer, round: LoveLetterRound) -> _T.NoReturn:
        card = player.get_card()
        player.lay_card()
        
        char_rule = mapper.get_map_by_character(card.get_character()).get_rule()
        
        await char_rule.execute_on_discarded(notifier, self, player)
    
    def is_finished(self, round: LoveLetterRound) -> bool:
        return len(round.get_alive_players()) <= 1
    
    
    
    


