from love_letter.enum import *

from love_letter.board import *

import typing as _T

class LoveLetterRoundsConfiguration():
    def __init__(self, equality_policy: LOVE_LETTER_ROUNDS_EQUALITY_POLICY):
        self._equality_policy = equality_policy
    
    def get_equality_policy(self) -> LOVE_LETTER_ROUNDS_EQUALITY_POLICY:
        return self._equality_policy

LOVE_LETTER_ROUNDS_CONFIGURATION_DEFAULT = LoveLetterRoundsConfiguration(
    LOVE_LETTER_ROUNDS_EQUALITY_POLICY.WIN_TOGETHER
)

