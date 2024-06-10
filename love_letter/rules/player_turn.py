import re
from ..mapping import *
from ..notifiers import *
from ..objects import *

from .character import *

import typing as _T

class LoveLetterPlayerTurnRule():
    def __init__(self):
        pass
    
    async def play(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        
        if player.is_protected():
            player.stop_protection()
        
        confirmed = False
        
        while not confirmed:
            card_result = await notifier.choose_card_to_play(player)
            
            if card_result[ "card" ] == "hand_card":
                card = player.get_card()
            else:
                card = player.get_drawn_card()
            
            card_map = mapper.get_map_by_character( card.get_character() )
            card_rule = card_map.get_rule()
            
            safe_state = card_rule.can_be_safely_laid(mapper, notifier, round)
            
            if safe_state == LOVE_LETTER_CHARACTER_RULE_SAFE:
                confirmed = True
            else:
                reason = ClientReason(LOVE_LETTER_REASON_UNSAFE_PLAY, {
                    'unsafe_status' : safe_state
                })
                if safe_state == LOVE_LETTER_CHARACTER_RULE_UNSAFE_COUNTESS_PRESENCE:
                    await notifier.display_unsafe_message(player, reason)
                    confirmed = False
                else:
                    answer = await notifier.confirm_unsafe_message(player, reason)
                    confirmed = answer.get_args()[ "confirmed" ]
        
        await card_rule.execute_on_player_turn(notifier, round)
    

