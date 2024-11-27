from .client import *

from ..objects import *

import socket as _socket
import asyncio as _asyncio

class ServerLogic():
    def __init__(self):
        pass
    
    def init_connection(self, server: Server) -> None:
        if server.is_ssl():
            bind = server._context.wrap_socket(_socket.socket(), server_side=True)
        else:
            bind = _socket.socket()
            
        bind.settimeout( 0.1 )
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
                await _asyncio.sleep(0.1)
        finally:
            await self.exit(server)
    
    async def accept_client(self, server: Server, world: World) -> None:
        loop = _asyncio.get_event_loop()
        try:
            conn, address = server.get_binding_connection().accept()
            conn.settimeout( 0.1 )
            client = server.get_clients().create_new_client(conn, address)
            
            print("Client {} received!".format(client.get_id()))
            
            loop.create_task(self.main_client(server, client, world))
            
        except _socket.timeout:
            return
    
    async def main_client(self, server: Server, client: Client, world: World) -> None:
        print("Client {} is now starting".format(client.get_id()))
        rule = ClientLogic()
        try:
            await rule.main_client(client, world)
        finally:
            await self.close_client(server, client)
            print("Client {} is now terminated".format(client.get_id()))
    
    async def close_client(self, server: Server, client: Client) -> None:
        await ClientLogic().close_client(client)
        
        server.get_clients().remove_client(client.get_id())
    
    async def exit(self, server: Server) -> None:
        for client in server.get_clients():
            await self.close_client(server, client)
        
        server.get_binding_connection().close()
    
