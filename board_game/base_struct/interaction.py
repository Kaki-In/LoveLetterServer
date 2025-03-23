from .message import *
from .task import *
from .response import *

from board_game.board import *

import typing as _T

_response_type = _T.TypeVar('_response_type', bound=BoardGameClientResponse)
_board_type = _T.TypeVar('_board_type', bound=BoardGameBoard)
_task_type = _T.TypeVar('_task_type', bound=BoardGameTask)

class BoardGameClientInteraction(BoardGameClientMessage, _T.Generic[_response_type, _board_type, _task_type]):
    def __init__(self, board: _board_type, task: _task_type):
        self._board = board
        self._task = task

    def get_board(self) -> _board_type:
        return self._board
    
    def get_task(self) -> _task_type:
        return self._task
    
    def json_to_response(self, json_data) -> _response_type:
        raise TypeError("this interaction does not make sense for " + type(self).__name__)
    
