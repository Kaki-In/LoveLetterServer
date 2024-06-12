from .client import *

import typing as _T
import asyncio as _asyncio

class ClientsList():
    def __init__(self):
        self._clients: dict[int, Client] = { }
        self._last_id: int = 0
    
    def get_client_by_id(self, id: int) -> Client:
        return self._clients[ id ]
    
    def create_new_client(self, reader: _asyncio.StreamReader, writer: _asyncio.StreamWriter) -> Client:
        cid = self._last_id
        self._last_id += 1
        
        client = Client(cid, reader, writer)
        
        self._clients[ cid ] = client
        
        return client
    
    def remove_client(self, id: int) -> None:
        del self._clients[id]
    
    def __iter__(self) -> _T.Iterator[Client]:
        return iter([self._clients[ id ] for id in self._clients])
    
