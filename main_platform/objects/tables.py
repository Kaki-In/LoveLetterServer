import random as _random

from .table import *

import typing as _T

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

        print("Table created")
        
        return name
    
    def get_table_by_name(self, name: str) -> Table:
        return self._tables[ name ]
    
    def get_waiting_tables(self) -> list[Table]:
        tables = []
        for table_id in self._tables:
            table = self._tables[table_id]
            if table.get_state() == TABLE_STATE_WAITING:
                tables.append(table)
        
        return tables
    
    def get_table_by_client(self, client: Client) -> _T.Optional[Table]:
        for table_id in self._tables:
            table = self._tables[table_id]
            
            if client in table.get_ghosts() + table.get_players():
                return table
    
