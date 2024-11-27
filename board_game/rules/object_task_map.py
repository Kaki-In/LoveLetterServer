from ..objects.context import *
from .task import *

import typing as _T

_object_type = _T.TypeVar('_object_type')
_tasks_type = _T.TypeVar('_tasks_type', bound = BoardGameTask)

class BoardGameObjectTasksMap(_T.Generic[_object_type, _tasks_type]):
    def __init__(self) :
        self._tasks: dict[_object_type, type[_tasks_type]] = {}

    def add_task(self, task: _object_type, rule: type[_tasks_type]) -> None:
        self._tasks[task] = rule

    def get_task(self, object: _object_type, **args) -> _tasks_type:
        return self._tasks[object](**args)
