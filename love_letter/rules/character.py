from ..objects import *
from ..notifiers import *

import typing as _T

LOVE_LETTER_CHARACTER_RULE_UNSAFE_NO_TARGET         = 0
LOVE_LETTER_CHARACTER_RULE_UNSAFE_SELF_IS_TARGET    = 1
LOVE_LETTER_CHARACTER_RULE_UNSAFE_COUNTESS_PRESENCE = 2
LOVE_LETTER_CHARACTER_RULE_UNSAFE_IS_SUICIDE        = 3
LOVE_LETTER_CHARACTER_RULE_SAFE                     = 4

def _abstract_async_method(f):
    async def raiseNotImplemented(*a, **b) -> _T.Any:
        raise NotImplementedError("This class is only abstract. Please use your own client")
    
    return raiseNotImplemented

def _abstract_method(f):
    def raiseNotImplemented(*a, **b) -> _T.Any:
        raise NotImplementedError("This class is only abstract. Please use your own client")
    
    return raiseNotImplemented

class LoveLetterCharacterRule():
    def __init__(self):
        pass
    
    @_abstract_async_method
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> _T.NoReturn:
        pass
    
    @_abstract_async_method
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    @_abstract_method
    def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        return True
    
    async def choose_player_between(self, round: LoveLetterRound, notifier: LoveLetterNotifier, players: LoveLetterPlayer, reason: ClientReason) -> LoveLetterPlayer:
        active_player = round.get_active_player()
        
        chosen_player = await notifier.choose_player_between(active_player, players, reason)
        target_player = round.get_player_by_id( chosen_player.get_args()[ "player_id" ] )
        
        return target_player
    
    async def choose_character(self, mapper: LoveLetterCharacterMapper, round: LoveLetterRound, notifier: LoveLetterNotifier, reason: ClientReason) -> LoveLetterCharacter:
        active_player = round.get_active_player()
        
        chosen_character = await notifier.choose_character(active_player, reason)
        target_character = mapper.get_map_by_character_name( chosen_character[ "character_name" ] )
        
        return target_character
    
    async def displayCard(self, round: LoveLetterRound, notifier: LoveLetterNotifier, card: LoveLetterCard, reason: ClientReason) -> _T.NoReturn:
        player = round.get_active_player()
        await notifier.display_card(player, card, reason)
    
    async def compare_cards(self, notifier: LoveLetterNotifier, player1: LoveLetterPlayer, player2: LoveLetterPlayer, reason: ClientReason) -> _T.NoReturn:
        await notifier.compare_cards(player1, player2, reason)
        

class LoveLetterGuardRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return
        
        reason1 = ClientReason(LOVE_LETTER_REASON_GUARD, {})
        
        target_player = await self.choose_player_between(round, notifier, avails, reason1)
        
        reason2 = ClientReason(LOVE_LETTER_REASON_GUARD, {
            'player': target_player.get_id()
        })
        
        target_character = await self.choose_character(mapper, round, notifier, reason2)
        
        player_card = target_player.get_card()
        
        if player_card.get_character() == target_character:
            target_player.eliminate()
        
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_NO_TARGET
        
        return LOVE_LETTER_CHARACTER_RULE_SAFE
    
class LoveLetterPriestRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return 
        
        reason = ClientReason(LOVE_LETTER_REASON_PRIEST, {})
        
        target_player = await self.choose_player_between(round, notifier, avails, reason)
        
        reason = ClientReason(LOVE_LETTER_REASON_PRIEST, {
            'player': target_player.get_id()
        })
        
        await self.displayCard(round, notifier, target_player.get_card(), reason)
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_NO_TARGET
        
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterBaronRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return
        
        reason = ClientReason(LOVE_LETTER_REASON_BARON, {})
        
        target_player = await self.choose_player_between(round, notifier, avails, reason)
        
        player_card = player.get_card()
        target_card = target_player.get_card()
        
        await self.compare_cards(notifier, player, target_player, reason)
        
        if player_card > target_card:
            await target_player.eliminate()
        
        elif player_card < target_card:
            await player.eliminate()
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_NO_TARGET
        
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterHandMaidRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        player.protect()
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterPrinceRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        avails = round.get_available_players()
        
        reason = ClientReason(LOVE_LETTER_REASON_PRINCE, {})
        
        target_player = await self.choose_player_between(round, notifier, avails, reason)
        
        await round.make_player_discard(target_player)
        
        if not target_player.is_eliminated():
            target_player.take_card( round.draw() )
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        player = round.get_active_player()
        
        if LOVE_LETTER_CHARACTER_COUNTESS in ( player.get_card().get_character(), player.get_drawn_card().get_character()):
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_COUNTESS_PRESENCE
        
        avails = list(round.get_available_players())
        
        if avails == [ player ]:
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_SELF_IS_TARGET
        
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterKingRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        player = round.get_active_player()
        
        avails = list(round.get_available_players())
        avails.remove(player)
        
        if not avails:
            return
        
        reason = ClientReason(LOVE_LETTER_REASON_KING, {})
        
        target_player = await self.choose_player_between(round, notifier, avails, reason)
        
        player_card = player.get_card()
        target_card = target_player.get_card()
        
        player.lay_card()
        target_player.lay_card()
        
        player.take_card(target_card)
        target_player.take_card(player_card)
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        player = round.get_active_player()
        
        if LOVE_LETTER_CHARACTER_COUNTESS in ( player.get_card().get_character(), player.get_drawn_card().get_character()):
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_COUNTESS_PRESENCE
        
        avails = list(round.get_available_players())
        
        if avails == [player]:
            return LOVE_LETTER_CHARACTER_RULE_UNSAFE_SELF_IS_TARGET
        
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterCountessRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        pass
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        pass
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        return LOVE_LETTER_CHARACTER_RULE_SAFE

class LoveLetterPrincessRule(LoveLetterCharacterRule):
    def __init__(self):
        super().__init__()
    
    async def execute_on_player_turn(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> _T.NoReturn:
        pass
    
    async def execute_on_discarded(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound, player: LoveLetterPlayer) -> _T.NoReturn:
        player.eliminate()
    
    async def can_be_safely_laid(self, mapper: LoveLetterCharacterMapper, notifier: Notifier, round: LoveLetterRound) -> bool:
        return LOVE_LETTER_CHARACTER_RULE_UNSAFE_IS_SUICIDE

