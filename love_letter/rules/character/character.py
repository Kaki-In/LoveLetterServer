from love_letter.base_struct.rule import *
from love_letter.tasks import *
from .choose import *

import typing as _T

_char_type = _T.TypeVar("_char_type", bound=LoveLetterCharacterTask)

class LoveLetterCharacterRule(_T.Generic[_char_type], LoveLetterRule[_char_type]):
    def get_effective_player(self) -> LoveLetterPlayer:
        return self.get_task().get_effective_player()
