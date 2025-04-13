from board_game.base_struct.task import *

import typing as _T

_object_type = _T.TypeVar('_object_type')
_tasks_type = _T.TypeVar('_tasks_type', bound = BoardGameTask)

class BoardGameObjectTasksMap(_T.Generic[_object_type, _tasks_type]):
    """
    This map allows to link objects with their corresponding tasks. 
    
    For exemple, an task to execute after having laid down a certain card. 
    """

    def __init__(self) :
        self._tasks: dict[_object_type, type[_tasks_type]] = {}

    def add_task(self, task: _object_type, rule: type[_tasks_type]) -> None:
        """
        Adds a task-object correspondance to the map. 
        """
        self._tasks[task] = rule

    def get_task(self, object: _object_type, **args) -> _tasks_type:
        """
        Returns the task corresponding to the given object. 
        """
        return self._tasks[object](**args)
