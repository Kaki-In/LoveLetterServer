from .context import *
from .clients import *

class LoveLetterGame():
    def __init__(self, context: LoveLetterGameContext, clients: list[LoveLetterClient]):
        self._context = context
        self._clients = clients
    
    def get_context(self) -> LoveLetterGameContext:
        return self._context
    
    def get_clients(self) -> list[LoveLetterClient]:
        return self._clients
