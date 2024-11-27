from .context.context import *

import board_game as _board_game

class LoveLetterTable(_board_game.BoardGameTable):
    def __init__(self, context: LoveLetterGameContext, clients: list[_board_game.BoardGameClient]):
        super().__init__(context, clients)
        self._context = context
        self._clients = clients
    
    def get_context(self) -> LoveLetterGameContext:
        return self._context
    
    def get_clients(self) -> list[_board_game.BoardGameClient]:
        return self._clients
