from .task import *
from .action import *
from .response import *
from .interaction import *
from .context import *

import typing as _T

_task_type = _T.TypeVar('_task_type', bound=BoardGameTask)
_general_task_type = _T.TypeVar('_general_task_type', bound=BoardGameTask)
_context_type = _T.TypeVar('_context_type', bound=BoardGameContext)
_actions_type = _T.TypeVar("_actions_type", bound=BoardGameAction)

class BoardGameRule(_T.Generic[_task_type, _general_task_type, _context_type, _actions_type]):
    """
    This class defines the rules that must be executed when a task has to be done. 
    """

    def __init__(self, task: _task_type):
        self._task = task
    
    def get_task(self) -> _task_type:
        """
        Returns the task that the rule is attempting to fill. 
        """
        return self._task

    def should_be_played_again(self, context: _context_type) -> bool:
        """
        True if the rule should be played again, False if it should not.
        This function is not called at the first execution. 
        
        Executed in the same way that a do while loop.
        """
        return False
    
    def execute_start(self, context: _context_type) -> list[_actions_type]:
        """
        Executes what to do before starting the rule
        """
        return []
    
    def execute_end(self, context: _context_type) -> list[_actions_type]:
        """
        Executes what to do when ending the rule
        """
        return []
    
    def get_tasks(self, context: _context_type) -> list[_general_task_type]:
        """
        Returns the tasks to execute.
        """

        return []
