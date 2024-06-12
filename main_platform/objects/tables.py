import random as _random

from .table import *

class TablesList():
    def __init__(self):
        self._tables: dict[str, Table] = {}
    
    def get_unused_name(self) -> str:
        while True:
            name = ""
            for i in range(10):
                name += _random.choice("abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "0123456789")
            
            if not name in self._tables:
                return name
    
    def create_table(self) -> str:
        table = Table()
        name = self.get_unused_name()
        self._tables[name] = table
        
        return name
    
    def get_table_by_name(self, name: str) -> Table:
        return self._tables[ name ]
    
