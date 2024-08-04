from .task import *
from .result import *

from ..objects.context import *

class LoveLetterRule():
    def __init__(self):
        pass

    def should_be_played_again(self, context: LoveLetterGameContext, results: tuple[LoveLetterResult]) -> bool:
        """
        True if the rule should be played again, False if it should not.
        This function is not called at the first execution. 
        
        Executed in the same way that a while loop.
        """
        return False

    def get_next_task(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        """
        Returns the tasks to execute.
        """

        return []
    
    def get_result(self, context: LoveLetterGameContext) -> LoveLetterResult:
        """
        Returns the result of the task.
        """

        return LoveLetterResult()
