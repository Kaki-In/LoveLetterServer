from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

import random as _random

class LoveLetterGameRule(LoveLetterRule):
    def __init__(self, task: LoveLetterPlayGameTask, criteria: LoveLetterCriteria):
        LoveLetterRule.__init__(self, task, criteria)

        self._state = task.get_state()

    def should_be_played_again(self, context: LoveLetterGameContext) -> bool:
        winners = self.get_winners(context)
        return len(winners) == 0
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        if self._state.is_initialized():
            actual_round_state = self._state.get_round_state()
            pass
        else:
            first_player = _random.choice(context.get_board().get_players())

        self._state.initialize(LoveLetterRoundState(first_player))

        return []
    
    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        return [
            LoveLetterPlayRoundTask(self._state.get_round_state()),
        ]
    
    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        print("Executing end of Game rule")

        winners = self.get_winners(context)

        return [
            LoveLetterEndGameAction(winners)
        ]
    
    def get_winners(self, context: LoveLetterGameContext) -> list[LoveLetterPlayer]:
        max_rounds_count = self.get_max_rounds_count(context)

        board = context.get_board()

        players = []

        for player in board.get_players():
            if player.get_won_rounds() >= max_rounds_count:
                players.append(player)
        
        return players
    
    def get_max_rounds_count(self, context: LoveLetterGameContext) -> int:
        configuration = context.get_configuration()
        game_configuration = configuration.get_game_configuration()

        if game_configuration.has_max_rounds_imposed():
            return game_configuration.get_max_rounds()
        
        board = context.get_board()
        players_count = len(board.get_players())

        if   players_count == 2:
            return 7
        
        elif players_count == 3:
            return 5
        
        elif players_count == 4:
            return 4
        
        raise ReferenceError('there is no default rounds count for this number of players')


