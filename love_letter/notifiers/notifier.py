from .client import *
from .message import *
from .result import *
from .reason import *

import typing as _T
import asyncio as _asyncio

LOVE_LETTER_MESSAGE_DISPLAY_CARD                = "display.card"
LOVE_LETTER_MESSAGE_CHOOSE_PLAYER               = "choose.player"
LOVE_LETTER_MESSAGE_CHOOSE_CHARACTER            = "choose.character"
LOVE_LETTER_MESSAGE_CHOOSE_CARD_TO_PLAY         = "choose.card_to_play"
LOVE_LETTER_MESSAGE_SET_PROTECTED               = "set_player.protected"
LOVE_LETTER_MESSAGE_SET_ELIMINATED              = "set_player.eliminated"
LOVE_LETTER_MESSAGE_COMPARE                     = "compare_cards"
LOVE_LETTER_MESSAGE_CONFIRM_UNSAFE              = "unsafe_play.confirm"
LOVE_LETTER_MESSAGE_DISPLAY_UNSAFE               = "unsafe_play.display"

LOVE_LETTER_REASON_GUARD                        = "character.guard"
LOVE_LETTER_REASON_PRIEST                       = "character.priest"
LOVE_LETTER_REASON_BARON                        = "character.baron"
LOVE_LETTER_REASON_PRINCE                       = "character.prince"
LOVE_LETTER_REASON_KING                         = "character.king"
LOVE_LETTER_REASON_UNSAFE_PLAY                  = "unsafe_play"

class Notifier():
    def __init__(self):
        self._clients: dict[int, LoveLetterClient] = {}
    
    def plug_client_with_player(self, client: LoveLetterClient, player: LoveLetterPlayer) -> None:
        self._clients[ player.get_id() ] = client
    
    def get_client_by_player(self, player: LoveLetterPlayer) -> LoveLetterClient:
        return self._clients[ player.get_id() ]
    
    async def notify_to_all(self, message: ClientMessage) -> None:
        tasks = []
        for client_id in self._clients:
            client = self._clients[ client_id ]
            tasks.append( client.send_message(message) )
        
        await _asyncio.gather(*tasks)
    
    async def send_message_to_client(self, player: LoveLetterPlayer, message: ClientMessage):
        client = self.get_client_by_player(player)
        await client.send_message(message)
    
    async def interact_with_client(self, player: LoveLetterPlayer, message: ClientMessage):
        client = self.get_client_by_player(player)
        await client.send_message(message)

class LoveLetterNotifier(Notifier):
    def __init__(self):
        super().__init__()
    
    async def display_card(self, player: LoveLetterPlayer, card: LoveLetterCard, reason: ClientReason) -> _T.NoReturn:
        message = ClientMessage(LOVE_LETTER_MESSAGE_DISPLAY_CARD,{
            'character' : card.get_character().get_name(),
            'reason'    : reason.toJson()
        })
        
        client = self.get_client_by_player(player)
        await client.interact(message)
    
    async def choose_player_between(self, player: LoveLetterPlayer, players: list[LoveLetterPlayer], reason: ClientReason) -> ClientResult:
        ids = [player.get_id() for player in players]
        
        message = ClientMessage(LOVE_LETTER_MESSAGE_CHOOSE_PLAYER, {
            'players' : ids,
            'reason'  : reason.toJson()
        })
        
        client = self.get_client_by_player(player)
        return await client.interact(message)
    
    async def choose_character(self, player: LoveLetterPlayer, reason: ClientReason) ->  ClientResult:
        message = ClientMessage(LOVE_LETTER_MESSAGE_CHOOSE_CHARACTER, {
            'reason': reason.toJson()
        })
        
        client = self.get_client_by_player(player)
        return await client.interact(message)
    
    async def choose_card_to_play(self, player: LoveLetterPlayer) -> ClientResult:
        card = player.get_card()
        drawn_card = player.get_drawn_card()
        message = ClientMessage(LOVE_LETTER_MESSAGE_CHOOSE_CARD_TO_PLAY, {
            'card'       : card.get_character().get_name(),
            'drawn_card' : drawn_card.get_character().get_name()
        })
        
        client = self.get_client_by_player(player)
        result = await client.interact(message)
        
        return result
    
    async def update_player_protection(self, player: LoveLetterPlayer) -> _T.NoReturn:
        message = ClientMessage(LOVE_LETTER_MESSAGE_SET_PROTECTED, {
            'player' : player.get_id(),
            'status' : player.is_protected()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            client.send_message(message)
    
    async def set_player_as_eliminated(self, player: LoveLetterPlayer) -> _T.NoReturn:
        message = ClientMessage(LOVE_LETTER_MESSAGE_SET_ELIMINATED, {
            'player' : player.get_id(),
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            client.send_message(message)
    
    async def compare_cards(self, player1: LoveLetterPlayer, player2: LoveLetterPlayer, reason: ClientReason) -> _T.NoReturn:
        message = ClientMessage(LOVE_LETTER_MESSAGE_COMPARE, {
            'player1' : player1.get_id(),
            'player1_card' : player1.get_card().get_character().get_name(),
            'player2' : player2.get_id(),
            'player2_card' : player2.get_card().get_character().get_name(),
            'reason'  : reason.toJson()
        })
        
        return await _asyncio.gather(self.interact_with_client(player1, message), self.interact_with_client(player2, message))
    
    async def display_unsafe_message(self, player: LoveLetterPlayer, reason: ClientReason) -> _T.NoReturn:
        message = ClientMessage(LOVE_LETTER_MESSAGE_DISPLAY_UNSAFE, {
            'reason'    : reason.toJson()
        })
        
        client = self.get_client_by_player(player)
        await client.interact(message)
    
    async def confirm_unsafe_message(self, player: LoveLetterPlayer, reason: ClientReason) -> ClientResult:
        message = ClientMessage(LOVE_LETTER_MESSAGE_CONFIRM_UNSAFE, {
            'reason'    : reason.toJson()
        })
        
        client = self.get_client_by_player(player)
        return await client.interact(message)
    
    






