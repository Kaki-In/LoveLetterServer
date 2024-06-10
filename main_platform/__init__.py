from .world import *
from .server import *

class Platform():
    def __init__(self):
        self._world = World()
        self._server = Server()
