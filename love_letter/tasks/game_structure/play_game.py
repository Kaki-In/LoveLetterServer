from love_letter.base_struct.task import *
from love_letter.states import *
from love_letter.objects import *

class LoveLetterPlayGameTask(LoveLetterTask):
    def __init__(self):
        LoveLetterTask.__init__(self)
        self._state = LoveLetterGameState()
    
    def get_state(self) -> LoveLetterGameState:
        return self._state
    
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

