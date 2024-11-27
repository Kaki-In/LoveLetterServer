from .context import *
from .clients import *

class BoardGameTable():
    def __init__(self, context: BoardGameContext, clients: list[BoardGameClient]):
        self._context = context
        self._clients = clients
    
    def get_context(self) -> BoardGameContext:
        return self._context
    
    def get_clients(self) -> list[BoardGameClient]:
        return self._clients
