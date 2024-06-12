from .tables import *

class World():
    def __init__(self):
        self._tables = TablesList()
    
    def get_tables(self):
        return self._tables
    

