from love_letter.actions import *

from .character import *

class LoveLetterPlayGuardCharacterRule(LoveLetterCharacterRule[LoveLetterPlayGuardCharacterTask]):
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        if len(self.get_task().get_state().get_chosable_players()) > 0:
            return [
                LoveLetterSeePlayerTask(self.get_effective_player(), self.get_task().get_state())
            ]
        
        else: # no player to choose, maybe others are securized
            return []

