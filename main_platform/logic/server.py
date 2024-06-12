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
    
    def should_stop(self) -> bool:
        return False
    
    async def main(self, server: Server, world: World) -> None:
        self.init_connection(server)
        
        try:
            while not self.should_stop():
                await self.accept_client(server, world)
        finally:
            await self.exit(server)
    
    async def accept_client(self, server: Server, world: World) -> None:
        loop = _asyncio.get_event_loop()
        try:
            conn, address = server.get_binding_connection().accept()
            client = server.get_clients().create_new_client(conn, address)
            
            loop.create_task(self.main_client(server, client, world))
            
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
    
    async def exit(self, server: Server) -> None:
        for client in server.get_clients():
            await self.close_client(server, client)
    
