from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

import random as _random

class LoveLetterGameRule(LoveLetterRule[LoveLetterPlayGameTask]):
    def should_be_played_again(self, context: LoveLetterContext) -> bool:
        winners = self.get_task().get_state().get_winners()
        return len(winners) == 0
    
    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        game_state = self.get_task().get_state()

        if game_state.has_round_defined():
            winners = game_state.get_actual_round().get_winners(context)

            if len(winners) > 1:
                max_cards_count = sum([card.get_character().get_value() for card in winners[0].get_discard()])

                for player in winners[1:]:
                    cards_count = sum([card.get_character().get_value() for card in player.get_discard()])

                    if cards_count > max_cards_count:
                        max_cards_count = cards_count
                
                winners = [player for player in winners if sum([card.get_character().get_value() for card in player.get_discard()]) == max_cards_count]

            if len(winners) > 0:
                if game_state.get_actual_round().get_player() in winners:
                    first_player = game_state.get_actual_round().get_player()
                else:
                    first_player = _random.choice(winners)
            else:
                first_player = _random.choice(context.get_board().get_alive_players())

        else:
            first_player = _random.choice(context.get_board().get_alive_players())
        
        return [
            LoveLetterPlayRoundTask(LoveLetterRoundState(first_player)),
        ]
    
    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        print("Executing end of Game rule")

        winners = self.get_task().get_state().get_winners()

        return [
            LoveLetterEndGameAction(winners)
        ]
    
