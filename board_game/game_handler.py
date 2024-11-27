from .tasks_queue import *

from .rules import *
from .objects import *
from .enum import *

class BoardGameHandler():
    def __init__(self, context: BoardGameContext, rules: BoardGameRuleMap):
        self._context = context
        self._rules = rules

        self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_IDLE

        self._tasks_queues = [BoardGameTasksQueue()]
    
    def get_context(self) -> BoardGameContext:
        return self._context
    
    def get_rules(self) -> BoardGameRuleMap:
        return self._rules
    
    def is_terminated(self) -> bool:
        return not self._tasks_queues[0].contains_tasks()
    
    def requires_interaction(self) -> bool:
        if self.is_terminated():
            return False
        
        task = self._tasks_queues[-1].get_actual_task()
        rule = self._rules.get_rule(task)

        return rule.requires_players_interaction(self._context)
    
    def get_required_interaction(self) -> BoardGameClientInteraction:
        task = self._tasks_queues[-1].get_actual_task()
        rule = self._rules.get_rule(task)

        return rule.get_interaction_subject(self._context)
    
    def get_waiting_task(self) -> BoardGameTask:
        return self._tasks_queues[-1].get_actual_task()
    
    def main_once(self) -> list[BoardGameAction]:
        actions: list[BoardGameAction] = []

        while not self.is_terminated():
            tasks_queue = self._tasks_queues[-1]

            if tasks_queue.contains_tasks():
                task = tasks_queue.get_actual_task()
                rule = self._rules.get_rule(task)

                if self._last_rule_state == BOARD_GAME_RULE_STATE.STATE_IDLE:
                    self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_STARTING
                    actions += rule.execute_start(self._context)
                    self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_RUNNING

                if rule.requires_players_interaction(self._context):
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

                self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_ENDING
                new_actions = rule.execute_end(self._context)

                actions += new_actions

                if rule.should_be_played_again(self._context):
                    self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_IDLE
                else:
                    tasks_queue.mark_actual_task_as_done()
                    self._last_rule_state = BOARD_GAME_RULE_STATE.STATE_RUNNING

        return actions
    
    def answer(self, response: BoardGameClientResponse) -> None:
        self._rules.get_rule(self.get_waiting_task()).execute_response(self._context, response)
    
    def add_main_task(self, task: BoardGameTask) -> None:
        self._tasks_queues[0].add_task(task)

    def add_specific_task(self, task: BoardGameTask) -> None:
        self._tasks_queues[-1].add_task(task)
    
