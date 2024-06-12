from ..objects import *

import asyncio as _asyncio
import love_letter as _love_letter
import json as _json

class ClientLogic():
    def __init__(self):
        pass
    
    async def close_client(self, client: Client):
        pass
    
    async def main_client(self, client: Client, world: World):
        pass
    
    async def receive_message(self, client: Client) -> _love_letter.ClientMessage:
        loop = _asyncio.get_event_loop()
        
        message = await loop.sock_recv(client.get_socket(), 1024)
        
        data = _json.loads(message)
        
        return data
    
