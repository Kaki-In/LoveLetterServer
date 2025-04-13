from .configuration import *

import typing as _T

_conf_type = _T.TypeVar("_conf_type")

class BoardGameContext(_T.Generic[_conf_type]):
    """
    Defines the context of the board game. 
    """

    def __init__(self, configuration: _conf_type) -> None:
        self._configuration = configuration

    def get_configuration(self) -> _conf_type:
        """
        Returns the configuration of the game context.
        """
        return self._configuration

