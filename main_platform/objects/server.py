from .clients import *

import ssl as _ssl
import socket as _socket
import typing as _T

class Server():
    def __init__(self, host: str, port: int, context: _ssl.SSLContext, ssl: bool = True):
        self._host: str = host
        self._port: int = port
        
        self._ssl_mode: bool = ssl
        
        self._context: _ssl.SSLContext = context
        
        self._bind: _T.Optional[_ssl.SSLSocket | _socket.socket] = None
        
        self._clients: ClientsList = ClientsList()
    
    def is_ssl(self) -> bool:
        return self._ssl_mode
    
    def get_host_name(self) -> str:
        return self._host
    
    def get_port(self) -> int:
        return self._port
    
    def get_context(self) -> _ssl.SSLContext:
        return self._context
    
    def get_clients(self) -> ClientsList:
        return self._clients
    
    def from_server_name(self, host: str, port: int, *server_names: str) -> 'Server':
        context = _ssl.SSLContext(_ssl.PROTOCOL_TLS_SERVER)
        for server_name in server_names:
            context.load_cert_chain(f'/etc/letsencrypt/live/{server_name}/fullchain.pem', f'/etc/letsencrypt/live/{server_name}/privkey.pem')
        
        return Server(host, port, context)
    
    def set_binding_connection(self, bind: _ssl.SSLSocket | _socket.socket) -> None:
        self._bind = bind
    
    def get_binding_connection(self) -> _ssl.SSLSocket | _socket.socket:
        if self._bind is None:
            raise ValueError("no binding connection given at this time")
        
        return self._bind
    
    def has_binding_connection(self) -> bool:
        return self._bind is not None
    
