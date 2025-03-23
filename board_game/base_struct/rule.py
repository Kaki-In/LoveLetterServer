from .task import *
from .action import *
from .response import *
from .criteria import *

from board_game.objects import *

import typing as _T

_criterias_type = _T.TypeVar('_criterias_type', bound=BoardGameCriteria)
_task_type = _T.TypeVar('_task_type', bound=BoardGameTask)

class BoardGameRule(_T.Generic[_criterias_type, _task_type]):
    def __init__(self, task: _task_type, criteria: _criterias_type):
        self._criteria = criteria
        self._task = task
    
    def get_task(self) -> _task_type:
        return self._task

    def get_criteria(self) -> _criterias_type:
        return self._criteria

    def should_be_played_again(self, context: BoardGameContext) -> bool:
        """
        True if the rule should be played again, False if it should not.
        This function is not called at the first execution. 
        
        Executed in the same way that a do while loop.
        """
        return False
    
    def execute_start(self, context: BoardGameContext) -> list[BoardGameAction]:
        """
        Executes what to do when starting the rule
        """
        return []
    
    def execute_response(self, context: BoardGameContext, response: BoardGameClientResponse) -> list[BoardGameAction]:
        """
        Executes what to do for a response to an interaction
        """
        return []
    
    def execute_end(self, context: BoardGameContext) -> list[BoardGameAction]:
        """
        Executes what to do when ending the rule
        """
        return []
    
    def requires_players_interaction(self, context: BoardGameContext) -> bool:
        return False
    
    def get_interaction_subject(self, context: BoardGameContext) -> BoardGameClientInteraction:
        """
        Returns the interaction that needs to be answered to continue the task
        """
        raise ValueError('this rule does not requires interaction')
    
    def get_tasks(self, context: BoardGameContext) -> list[BoardGameTask]:
        """
        Returns the tasks to execute.
        """

        return []
