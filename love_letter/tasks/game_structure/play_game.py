from love_letter.base_struct.task import *
from love_letter.states import *

class LoveLetterPlayGameTask(LoveLetterTask):
    def __init__(self, configuration: LoveLetterConfiguration, board: LoveLetterBoard):
        LoveLetterTask.__init__(self)
        
        self._state = LoveLetterGameState(configuration, board)
    
    def get_state(self) -> LoveLetterGameState:
        return self._state
