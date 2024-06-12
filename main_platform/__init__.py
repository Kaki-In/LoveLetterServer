from .objects import *
from .controllers import *
from .logic import *

class Platform():
    def __init__(self):
        self._main_world = self._world = World()
