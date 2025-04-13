import typing as _T

from .reason import *

class BoardGameClientMessage():
    """
    A simple message class, toward the client. 
    This class is purely abstract
    """

    def __init__(self):
        pass
    
    def toJson(self) -> _T.Any:
        """
        Returns the json object that would be sent to the client. 
        """

        return None
    