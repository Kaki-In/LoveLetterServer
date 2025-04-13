from .turn import *

from love_letter.base_struct.states import *
from love_letter.context import *

import typing as _T

class LoveLetterRoundState(LoveLetterState):
    def __init__(self, first_player: LoveLetterPlayer):
        self._player = first_player
    
    def set_player(self, player: LoveLetterPlayer):
        self._player = player

    def get_player(self) -> LoveLetterPlayer:
        return self._player
    
    def get_winners(self, context: LoveLetterContext) -> list[LoveLetterPlayer]:
        alive_players = context.get_board().get_alive_players()
        deck = context.get_board().get_deck()

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
    
