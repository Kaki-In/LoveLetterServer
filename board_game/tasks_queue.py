from .base_struct.rule import *

import typing as _T

_task_type = _T.TypeVar("_task_type", bound=BoardGameTask)

class BoardGameTasksQueue(_T.Generic[_task_type]):
    """
    This class describes a tasks queue that must be executed in a certain order.
    """

    def __init__(self):
        self._tasks: list[_task_type] = []
    
    def add_task(self, task: _task_type) -> None:
        """
        Adds a task to execute after the all others. 
        """
        self._tasks.append(task)
    
    def contains_tasks(self) -> bool:
        """
        Returns True when contains task to execute, False otherwise. 
        """
        return len(self._tasks) > 0
    
    def mark_actual_task_as_done(self) -> None:
        """
        Remove the current task to the tasks to execute list. 
        """
        self._tasks.pop(0)
    
    def get_actual_task(self) -> _task_type:
        """
        Returns the actual executing task. 
        """

        if not self.contains_tasks():
            raise ValueError("there is no task to do right now")
        
        return self._tasks[0] 
