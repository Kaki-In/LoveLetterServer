from .rule import *

from .task import *

class BoardGameRuleMap():
    def __init__(self) :
        self._protocols: dict[type[BoardGameTask], type[BoardGameRule]] = {}

    def add_rule(self, task: type[BoardGameTask], rule: type[BoardGameRule]) -> None:
        self._protocols[task] = rule

    def get_rule(self, task: BoardGameTask) -> BoardGameRule:
        return self._protocols[type(task)](task)
