from .task import *
from .action import *

import board_game as _board_game
from love_letter.context import *
from love_letter.base_struct.response import *
from love_letter.base_struct.interaction import *

import typing as _T

_task_type = _T.TypeVar("_task_type", bound=LoveLetterTask)

class LoveLetterRule(_T.Generic[_task_type], _board_game.BoardGameRule[_task_type, LoveLetterTask, LoveLetterContext, LoveLetterAction]):
    """

    This class represents board game rules, in the context of the love letter board game. 

    """
