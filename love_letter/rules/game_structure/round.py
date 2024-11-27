from love_letter.base_struct.rule import *
from love_letter.actions import *
from love_letter.tasks import *

class LoveLetterRoundRule(LoveLetterRule):
    def __init__(self, task: LoveLetterPlayRoundTask):
        super().__init__(task)

    def should_be_played_again(self, context: LoveLetterGameContext) -> bool:
        players = self.get_round_winners(context.get_board())

        return len(players) == 0
    
    def execute_start(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        print("Executing start of Round rule")

        self.prepare_cards(context)

        turn = LoveLetterTurnState(context.get_board().get_available_players()[0])
        context.get_state().get_round_state().mark_as_setupped(turn)

        return [LoveLetterNewRoundAction()]
    
    def prepare_cards(self, context: LoveLetterGameContext) -> None:
        deck = context.get_board().get_deck()

        deck.erase_all()

        for character, count in context.get_configuration().get_characters_configuration().get_characters():
            for _ in range(count):
                deck.add_card(LoveLetterCard(character))
        
        for player in context.get_board().get_players():
            while player.has_card():
                player.lay_card()
            
            player.take_card(deck.take_card())

    def get_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        state = context.get_state()
        round_state = state.get_round_state()
        turn_state = round_state.get_turn_state()
        player = turn_state.get_player()

        return [
            LoveLetterPlayTurnTask(player, turn_state),
        ]
    
    def execute_end(self, context: LoveLetterGameContext) -> list[LoveLetterAction]:
        print("Executing end of Round rule")
        return [LoveLetterPlayRoundAction()]

    def get_round_winners(self, board: LoveLetterBoard) -> list[LoveLetterPlayer]:
        alive_players = board.get_alive_players()
        deck = board.get_deck()

        if len(alive_players) <= 1:
            return alive_players
        
        if len(deck) > 0:
            return []
        
        max_char_value = 0
        max_players: list[LoveLetterPlayer] = []
        
        for player in alive_players:
            character = player.get_card().get_character()
            value = character.get_value()

            if value > max_char_value:
                max_char_value = value
                max_players = [player]
            
            elif value == max_char_value:
                max_players.append(player)
        
        if len(max_players) == 1:
            return max_players
        
        max_cards_count = -1
        last_max_players = []

        for player in alive_players:
            discard = player.get_discard()
            card_sum = 0

            for card in discard:
                card_sum += card.get_character().get_value()
            
            if card_sum > max_cards_count:
                max_cards_count = card_sum
                last_max_players = [player]
            
            elif card_sum == max_cards_count:
                last_max_players.append(player)
        
        return last_max_players
    


