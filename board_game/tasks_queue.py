from .rules import *

import typing as _T

class BoardGameTasksQueue():
    def __init__(self):
        self._tasks: list[BoardGameTask] = []
    
    def add_task(self, task: BoardGameTask) -> None:
        self._tasks.append(task)
    
    def contains_tasks(self) -> bool:
        return len(self._tasks) > 0
    
    def mark_actual_task_as_done(self) -> None:
        self._tasks.pop(0)
    
    def get_actual_task(self) -> BoardGameTask:
        if not self.contains_tasks():
            raise ValueError("there is no task to do right now")
        
        return self._tasks[0] 
