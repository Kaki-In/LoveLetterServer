from .client import *

from ..objects import *

import socket as _socket
import asyncio as _asyncio

class ServerLogic():
    def __init__(self):
        pass
    
    def init_connection(self, server: Server):
        bind = server._context.wrap_socket(_socket.socket(), server_side=True)
        bind.settimeout( 1 )
        bind.bind((server.get_host_name(), server.get_port()))
        bind.listen( 1000 )
        
        server.set_binding_connection(bind)
    
    async def accept_client(self, server: Server) -> None:
        loop = _asyncio.get_event_loop()
        try:
            conn, address = await loop.sock_accept( server.get_binding_connection() )
            server.get_clients().create_new_client(conn, address)
            
        except _socket.timeout:
            return
    
    async def main_client(self, server: Server, client: Client, world: World) -> None:
        rule = ClientLogic()
        try:
            await rule.main_client(client, world)
        finally:
            await self.close_client(server, client)
    
    async def close_client(self, server: Server, client: Client) -> None:
        await ClientLogic().close_client(client)
        
        server.get_clients().remove_client(client.get_id())
        
    
