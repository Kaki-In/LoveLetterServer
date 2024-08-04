from .rule import *

class LoveLetterRoundRule(LoveLetterRule):
    def __init__(self):
        super().__init__()

    def should_be_played_again(self, context: LoveLetterGameContext, results: tuple[LoveLetterResult, LoveLetterResult, LoveLetterResult, LoveLetterResult]) -> bool:
        players = self.get_round_winners(context.get_board())

        return len(players) == 0

    def get_next_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        state = context.get_state()
        round_state = state.get_round_state()
        turn_state = round_state.get_turn_state()
        player = turn_state.get_player()

        return [
            LoveLetterPlayerInitializationTask(player),
            LoveLetterPlayPlayerTask(player),
            LoveLetterPlayerTerminationTask(player),
            LoveLetterChangeActivePlayerTask()
        ]
    
    def get_round_winners(self, board: LoveLetterBoard) -> list[LoveLetterPlayer]:
        alive_players = board.get_alive_players()
        deck = board.get_deck()

        if len(alive_players) <= 1:
            return list(alive_players)
        
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
    
    def get_status(self, context: LoveLetterGameContext) -> LoveLetterRoundResult:
        winners = self.get_round_winners(context.get_board())

        return LoveLetterRoundResult(winners)



