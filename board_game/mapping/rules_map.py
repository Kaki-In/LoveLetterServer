from board_game.base_struct.rule import *
from board_game.base_struct.task import *

import typing as _T

_criterias_type = _T.TypeVar('_criterias_type', bound=BoardGameCriteria)

class BoardGameRuleMap(_T.Generic[_criterias_type]):
    def __init__(self, criteria: _criterias_type):
        self._criteria = criteria
        self._protocols: dict[type[BoardGameTask], type[BoardGameRule[_criterias_type, _T.Any]]] = {}

    def add_rule(self, task: type[BoardGameTask], rule: type[BoardGameRule]) -> None:
        self._protocols[task] = rule

    def get_rule(self, task: BoardGameTask) -> BoardGameRule:
        if not type(task) in self._protocols:
            raise ValueError("unknown task type : " + type(task).__name__)

        return self._protocols[type(task)](task, self._criteria)

