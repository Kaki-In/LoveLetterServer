from .tasks_queue import *

from .base_struct.rule import *
from .base_struct.interactive_rule import *
from .mapping import *
from .enum import *

import typing as _T

_task_type = _T.TypeVar("_task_type", bound = BoardGameTask)
_context_type = _T.TypeVar("_context_type", bound = BoardGameContext)
_actions_type = _T.TypeVar("_actions_type", bound=BoardGameAction)
_response_type = _T.TypeVar("_response_type", bound=BoardGameClientResponse)
_interaction_type = _T.TypeVar("_interaction_type", bound=BoardGameClientInteraction)

class BoardGameHandler(_T.Generic[_task_type, _context_type, _actions_type, _response_type, _interaction_type]):
    """
    This class allows to execute a game
    """

    def __init__(self, context: _context_type, rules: BoardGameRuleMap[_task_type, _context_type, _actions_type, _response_type, _interaction_type]):
        self._context = context
        self._rules = rules

        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_IDLE

        self._tasks_queues = [BoardGameTasksQueue[_task_type]()]
    
    def get_rules(self) -> BoardGameRuleMap[_task_type, _context_type, _actions_type, _response_type, _interaction_type]:
        """
        Returns the rules map of the game handler. 
        """
        return self._rules
    
    def is_terminated(self) -> bool:
        """
        Returns True when the game handler has finished the whole game
        """
        return not self._tasks_queues[0].contains_tasks()
    
    def requires_interaction(self) -> bool:
        """
        Returns True when the game handler needs a task interaction response to continue its execution, False otherwise
        """
        if self.is_terminated():
            return False
        
        task = self._tasks_queues[-1].get_actual_task()
        rule = self._rules.get_rule(task)

        if isinstance(rule, BoardGameInteractiveRule):
            return rule.requires_players_interaction(self._context)
        else:
            return False
    
    def get_required_interaction(self) -> _interaction_type:
        """
        Returs the interaction required by the actual task. 
        Please first call `requires_interaction` to ensure that there is one. 
        """

        task = self._tasks_queues[-1].get_actual_task()
        rule = self._rules.get_rule(task)

        if isinstance(rule, BoardGameInteractiveRule):
            return rule.get_interaction_subject(self._context)
        else:
            raise TypeError("not an interactive rule")
    
    def get_waiting_task(self) -> _task_type:
        """
        Returns the actual executed task. 
        Please first call `is_terminated` to ensure that there is one. 
        """
        return self._tasks_queues[-1].get_actual_task()
    
    def main_once(self) -> list[_actions_type]:
        """
        This function mains the game, and exits when an interaction is needed, or when there is nothing more to do.
        """

        try:
            actions: list[_actions_type] = []

            while not self.is_terminated():
                tasks_queue = self._tasks_queues[-1]

                if tasks_queue.contains_tasks():
                    task = tasks_queue.get_actual_task()
                    rule = self._rules.get_rule(task)

                    if self._last_rule_state == BOARD_GAME_RULE_STATE.STATE_IDLE:
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_STARTING
                        actions += rule.execute_start(self._context)
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_RUNNING

                    if isinstance(rule, BoardGameInteractiveRule) and rule.requires_players_interaction(self._context):
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_WAITING
                        break

                    self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_RUNNING

                    new_tasks_queue = BoardGameTasksQueue()
                    self._tasks_queues.append(new_tasks_queue)

                    for task in rule.get_tasks(self._context):
                        new_tasks_queue.add_task(task)
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_IDLE
                
                else:
                    self._tasks_queues.pop(-1)
                    tasks_queue = self._tasks_queues[-1]

                    task = tasks_queue.get_actual_task()
                    rule = self._rules.get_rule(task)

                    if rule.should_be_played_again(self._context):
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_RUNNING
                    else:
                        tasks_queue.mark_actual_task_as_done()

                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_ENDING

                        new_actions = rule.execute_end(self._context)
                        actions += new_actions
                        
                        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_IDLE
        
        except Exception:
            print("An error occured while running the tasks list " + repr(self._tasks_queues))
            raise

        return actions
    
    def answer(self, response: _response_type) -> None:
        """
        Answers a client response to the waiting interaction. 
        """
        rule = self._rules.get_rule(self.get_waiting_task())

        if not isinstance(rule, BoardGameInteractiveRule):
            raise TypeError("not an interactive rule")

        rule.execute_response(response, self._context)
    
    def add_main_task(self, task: _task_type) -> None:
        """
        Adds a task to execute after having terminated. 
        """
        self._tasks_queues[0].add_task(task)

    def add_specific_task(self, task: _task_type) -> None:
        """
        Adds a task to execute at the end of the current one. 
        """
        self._tasks_queues[-1].add_task(task)
    
