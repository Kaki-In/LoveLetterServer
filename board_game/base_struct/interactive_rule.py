from .rule import *

import typing as _T

_task_type = _T.TypeVar('_task_type', bound=BoardGameTask)
_general_task_type = _T.TypeVar('_general_task_type', bound=BoardGameTask)
_context_type = _T.TypeVar('_context_type', bound=BoardGameContext)
_actions_type = _T.TypeVar("_actions_type", bound=BoardGameAction)
_response_type = _T.TypeVar("_response_type", bound=BoardGameClientResponse)
_interaction_type = _T.TypeVar("_interaction_type", bound=BoardGameClientInteraction)

class BoardGameInteractiveRule(_T.Generic[_task_type, _general_task_type, _context_type, _actions_type, _response_type, _interaction_type], BoardGameRule[_task_type, _general_task_type, _context_type, _actions_type]):
    """
    This class defines the rules that must be executed when a task has to be done, with the specificity to be interactive toward an extern player. 
    """

    def execute_response(self, response: _response_type, context: _context_type) -> list[_actions_type]:
        """
        Executes what to do for a response to an interaction
        """
        return []
    
    def requires_players_interaction(self, context: _context_type) -> bool:
        """
        Returns True if the players needs interaction
        """
        return False
    
    def get_interaction_subject(self, context: _context_type) -> _interaction_type:
        """
        Returns the interaction that needs to be answered to continue the task
        """
        raise ValueError('this rule does not requires interaction')
    
