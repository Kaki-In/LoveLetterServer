from love_letter.rules import *
from love_letter.context import *

import board_game as _board_game

class LoveLetterRuleMap(_board_game.BoardGameRuleMap[LoveLetterTask, LoveLetterContext, LoveLetterAction, LoveLetterClientResponse, LoveLetterClientInteraction]):
    def __init__(self):
        _board_game.BoardGameRuleMap.__init__(self)

        self.add_rule(LoveLetterPlayGameTask, LoveLetterGameRule)
        self.add_rule(LoveLetterPlayRoundTask, LoveLetterRoundRule)
        self.add_rule(LoveLetterPlayTurnTask, LoveLetterTurnRule)

        self.add_rule(LoveLetterDrawCardTask, LoveLetterDrawCardRule)
        self.add_rule(LoveLetterChooseCardTask, LoveLetterChooseCardRule)

        self.add_rule(LoveLetterPlayChosenCardTask, LoveLetterPlayChosenCardRule)
        self.add_rule(LoveLetterDiscardTask, LoveLetterDiscardRule)

        self.add_rule(LoveLetterChoosePlayerTask, LoveLetterChoosePlayerRule)
        self.add_rule(LoveLetterArrestPlayerTask, LoveLetterArrestPlayerRule)

        self.add_rule(LoveLetterChooseCharacterTask, LoveLetterChooseCharacterRule)
        self.add_rule(LoveLetterPlayCharacterTask, LoveLetterPlayCharacterRule)
        self.add_rule(LoveLetterPlayGuardCharacterTask, LoveLetterPlayGuardCharacterRule)

