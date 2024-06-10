from .client import *
from .message import *

import typing as _T
import asyncio as _asyncio

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
    
    async def send_message_to_client(self, player, message: ClientMessage):
        client = self.get_client_by_player(player)
        await client.send_message(message)
    
    async def interact_with_client(self, player, message: ClientMessage):
        client = self.get_client_by_player(player)
        await client.send_message(message)
    


