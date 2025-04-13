from .rule import *

import board_game as _board_game
from board_game.base_struct import interactive_rule as _boardgame_interactive_rule
from love_letter.context import *
from love_letter.base_struct.response import *
from love_letter.base_struct.interaction import *

import typing as _T

_task_type = _T.TypeVar("_task_type", bound=LoveLetterTask)
_response_type = _T.TypeVar("_response_type", bound=LoveLetterClientResponse)
_interaction_type = _T.TypeVar("_interaction_type", bound=LoveLetterClientInteraction)

class LoveLetterInteractiveRule(_T.Generic[_task_type, _response_type, _interaction_type], LoveLetterRule[_task_type], _boardgame_interactive_rule.BoardGameInteractiveRule[_task_type, LoveLetterTask, LoveLetterContext, LoveLetterAction, _response_type, _interaction_type]):
    """

    This class represents board game interactive rules, in the context of the love letter board game. 

    """
