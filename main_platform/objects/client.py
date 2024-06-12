from .tables import *
from ..controllers.client import *

import socket as _socket
import ssl as _ssl
import typing as _T
import events as _events
import love_letter as _love_letter
import promisio as _promisio

class Client():
    def __init__(self, id: int, connection: _ssl.SSLSocket | _socket.socket, address):
        self._id: int = id
        self._socket: _ssl.SSLSocket | _socket.socket = connection
        
        self._client: DistantClient = DistantClient()
        
        self._name: str = "Invité " + str(id)
    
    def get_id(self) -> int:
        return self._id
    
    def get_socket(self) -> _ssl.SSLSocket | _socket.socket:
        return self._socket
    
    def get_game_client(self) -> DistantClient:
        return self._client
    
    def get_name(self) -> str:
        return self._name
    


