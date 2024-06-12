from .tables import *
from ..controllers.client import *

import socket as _socket
import ssl as _ssl
import typing as _T
import events as _events

class Client():
    def __init__(self, id: int, connection: _ssl.SSLSocket, address):
        self._id: int = id
        self._socket: _ssl.SSLSocket = connection
        self._client: DistantClient = DistantClient()
        
    def get_id(self) -> int:
        return self._id
    
    def get_socket(self) -> _ssl.SSLSocket:
        return self._socket
    
    def get_game_client(self) -> DistantClient:
        return self._client
    


