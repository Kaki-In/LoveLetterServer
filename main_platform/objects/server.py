from .clients import *

import ssl as _ssl
import typing as _T

class Server():
    def __init__(self, host: str, port: int, context: _ssl.SSLContext):
        self._host: str = host
        self._port: int = port
        self._context: _ssl.SSLContext = context
        
        self._bind: _T.Optional[_ssl.SSLSocket] = None
        
        self._clients: ClientsList = ClientsList()
    
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
    
    def set_binding_connection(self, bind: _ssl.SSLSocket) -> None:
        self._bind = bind
    
    def get_binding_connection(self) -> _T.Optional[_ssl.SSLSocket]:
        return self._bind
    
