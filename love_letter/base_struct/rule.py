from .task import *
from .action import *

from love_letter.objects import *

import board_game as _board_game

class LoveLetterRule(_board_game.BoardGameRule):
    def __init__(self, task: LoveLetterTask):
        super().__init__(task)

    def should_be_played_again(self, context: LoveLetterGameContext) -> bool:
        """
        True if the rule should be played again, False if it should not.
        This function is not called at the first execution. 
        
        Executed in the same way that a while loop.
        """
        return False

    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        """
        Executes what to do when starting the rule
        """
        return []
    
    def execute_response(self, context: LoveLetterGameContext, response: _board_game.BoardGameClientResponse) -> list[LoveLetterAction]:
        """
        Executes what to do for a response to an interaction
        """
        return []
    
    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        """
        Executes what to do when ending the rule
        """
        return []
    
    def requires_players_interaction(self, context: LoveLetterGameContext) -> bool:
        return False
    
    def get_interaction_subject(self, context: LoveLetterGameContext) -> _board_game.BoardGameClientInteraction:
        """
        Returns the interaction that needs to be answered to continue the task
        """
        raise ValueError('this protocol does not requires interaction')
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        """
        Returns the tasks to execute.
        """

        return []
            
