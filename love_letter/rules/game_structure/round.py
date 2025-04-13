from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

class LoveLetterRoundRule(LoveLetterRule[LoveLetterPlayRoundTask]):
    def should_be_played_again(self, context: LoveLetterContext) -> bool:
        players = self.get_task().get_round_state().get_winners(context)

        return len(players) == 0
    
    def execute_start(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        self.prepare_cards(context)

        return [LoveLetterNewRoundAction()]
    
    def prepare_cards(self, context: LoveLetterContext) -> None:
        deck = context.get_board().get_deck()

        deck.erase_all()

        for character, count in context.get_configuration().get_characters_configuration().get_characters():
            for _ in range(count):
                deck.add_card(LoveLetterCard(character))
        
        for player in context.get_board().get_players():
            while player.has_card():
                player.lay_card()
            
            player.take_card(deck.take_card())

    def get_tasks(self, context: LoveLetterContext) -> list[LoveLetterTask]:
        round_state = self.get_task().get_round_state()
        player = round_state.get_player()

        return [
            LoveLetterPlayTurnTask(player, LoveLetterTurnState(player)),
        ]
    
    def execute_end(self, context: LoveLetterContext) -> list[LoveLetterAction]:
        print("Executing end of Round rule")

        return [LoveLetterPlayRoundAction()]

