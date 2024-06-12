from .client_actions import *

from ..objects import *

import asyncio as _asyncio
import love_letter as _love_letter
import json as _json

class ClientLogic():
    def __init__(self):
        self._actions = ClientMainActions()
    
    async def close_client(self, client: Client):
        pass
    
    async def main_client(self, client: Client, world: World):
        loop = _asyncio.get_event_loop()
        
        game_client = client.get_game_client()
        
        while True:
            try:
                if game_client.messages_are_waiting():
                    await self.main_game_client_message(client, game_client)
                
                if game_client.interactions_are_waiting():
                    await self.main_game_client_interaction(client, game_client)
            except Exception as exc:
                pass
            
            try:
                message = await self.receive_message(client)
                if message == "":
                    break
                
                data = _json.loads(message)
                loop.create_task( self._actions.execute_action(data['name'], data['args'], client, world) )
                
            except Exception as exc:
                pass
    
    async def receive_message(self, client: Client) -> str:
        loop = _asyncio.get_event_loop()
        
        message = await loop.sock_recv(client.get_socket(), 1024)
        
        return message.decode()
    
    async def main_game_client_message(self, client: Client, game_client : DistantClient):
        message = game_client.get_next_message()
        
        data = {
            "name" : "game_message",
            "args": {
                "message": message.toJson()
            }
        }
        
        client.get_socket().send( _json.dumps(data).encode() )
    
    async def main_game_client_interaction(self, client: Client, game_client : DistantClient):
        id, message = game_client.get_next_interaction()
        
        data = {
            "name" : "game_interaction",
            "args": {
                "id": id,
                "message": message.toJson()
            }
        }
        
        client.get_socket().send( _json.dumps(data).encode() )
    
