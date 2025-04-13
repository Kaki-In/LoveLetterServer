from board_game.base_struct.rule import *
from board_game.base_struct.task import *

import typing as _T

_task_type = _T.TypeVar("_task_type", bound = BoardGameTask)
_specific_task_type = _task_type
_context_type = _T.TypeVar("_context_type", bound = BoardGameContext)
_actions_type = _T.TypeVar("_actions_type", bound=BoardGameAction)
_response_type = _T.TypeVar("_response_type", bound=BoardGameClientResponse)
_interaction_type = _T.TypeVar("_interaction_type", bound=BoardGameClientInteraction)

class BoardGameRuleMap(_T.Generic[_task_type, _context_type, _actions_type, _response_type, _interaction_type]):
    """
    This map allows to link tasks with their corresponding rules. 
    """
    def __init__(self):
        self._protocols: dict[type[_task_type], type[BoardGameRule[_specific_task_type, _T.Any, _context_type, _actions_type]]] = {}

    def add_rule(self, task: type[_specific_task_type], rule: type[BoardGameRule[_specific_task_type, _task_type, _context_type, _actions_type]]) -> None:
        """
        Adds a rule-task-type correspondance to the map. 
        """
        self._protocols[task] = rule

    def get_rule(self, task: _specific_task_type) -> BoardGameRule[_specific_task_type, _specific_task_type, _context_type, _actions_type]:
        """
        Returns the rule corresponding to a given task. 
        """
        if not type(task) in self._protocols:
            raise ValueError("unknown task type : " + type(task).__name__)

        return self._protocols[type(task)](task)

