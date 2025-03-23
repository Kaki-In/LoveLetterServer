from .state import *

from love_letter.enum import *
import typing as _T

_object_type = _T.TypeVar("_object_type")

class LoveLetterNeedingObjectState(LoveLetterState, _T.Generic[_object_type]):
    def __init__(self):
        LoveLetterState.__init__(self)

        self._object: _T.Optional[_object_type] = None

    def get_chosen_object(self) -> _object_type:
        if self._player_card is None:
            raise TypeError("this state has not been given an object yet")

        return self._player_card
    
    def set_chosen_object(self, player_card: _object_type):
        self._player_card = player_card

    def has_chosen_object(self) -> bool:
        return self._player_card is not None

