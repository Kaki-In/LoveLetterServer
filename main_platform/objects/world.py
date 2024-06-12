from .tables import *
from .server import *

class World():
    def __init__(self):
        self._tables = TablesList()
        
        self._clients = ClientsList()

