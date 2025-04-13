from .message import *
from .task import *
from .response import *
from .context import *

import typing as _T

_context_type = _T.TypeVar("_context_type", bound=BoardGameContext)
_response_type = _T.TypeVar('_response_type', bound=BoardGameClientResponse)
_task_type = _T.TypeVar('_task_type', bound=BoardGameTask)

class BoardGameClientInteraction(BoardGameClientMessage, _T.Generic[_response_type, _task_type, _context_type]):
    """

    Defines an interaction required to finish the execution of a task's rule.
    The BoardGameClientInteraction is executed in a certain context, regarding to certain task.

    """

    def __init__(self, task: _task_type):
        self._task = task

    def get_task(self) -> _task_type:
        """
        Returns the task of the task. 
        """

        return self._task
    
    def json_to_response(self, json_data, context: _context_type) -> _response_type:
        """
        Returns the BoardGameClientResponse object corresponding to the json data provided by the client
        """

        raise TypeError("this interaction does not make sense for " + type(self).__name__)
    
