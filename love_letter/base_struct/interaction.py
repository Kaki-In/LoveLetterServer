import board_game as _board_game
import typing as _T

from love_letter.board import *
from love_letter.base_struct.task import *

from .response import *

_response_type = _T.TypeVar('_response_type', bound=LoveLetterClientResponse)
_task_type = _T.TypeVar('_task_type', bound=LoveLetterTask)

class LoveLetterClientInteraction(_T.Generic[_response_type, _task_type], _board_game.BoardGameClientInteraction[_response_type, LoveLetterBoard, _task_type]):
    def __init__(self, board: LoveLetterBoard, task: LoveLetterTask):
        _board_game.BoardGameClientInteraction.__init__(self, board, task)

