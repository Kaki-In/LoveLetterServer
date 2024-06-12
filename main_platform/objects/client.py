from .tables import *
from ..controllers.client import *

import ssl as _ssl
import asyncio as _asyncio

class Client():
    def __init__(self, id: int, reader: _asyncio.StreamReader, writer: _asyncio.StreamWriter):
        self._id: int = id
        self._reader: _asyncio.StreamReader = reader
        self._writer: _asyncio.StreamWriter = writer
        
        self._client: DistantClient = DistantClient()
        
        self._name: str = "Invité " + str(id)
    
    def get_reader(self) -> _asyncio.StreamReader:
        return self._reader
    
    def get_writer(self) -> _asyncio.StreamWriter:
        return self._writer
    
    def get_id(self) -> int:
        return self._id
    
    def get_game_client(self) -> DistantClient:
        return self._client
    
    def get_name(self) -> str:
        return self._name
    
    def toJson(self):
        return {
            'id': self._id,
            'name': self._name
        }
    


