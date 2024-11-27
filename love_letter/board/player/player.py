from ..deck.card import *
import events as _events

class LoveLetterPlayer:
    def __init__(self, player_id: int, name: str):
        self._id: int = player_id
        self._card: LoveLetterCard | None = None
        self._drawn: LoveLetterCard | None = None
        self._is_protected: bool = False
        self._is_eliminated: bool = False
        self._discard: list[LoveLetterCard] = []
        self._won_rounds: int = 0
        self._name: str = name
        
    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def get_card(self) -> LoveLetterCard:
        if self._card is None:
            raise ValueError('player ' + str(self._id) + ' does not have any card')
        
        return self._card

    def get_drawn_card(self) -> LoveLetterCard:
        if self._drawn is None:
            raise ValueError('player ' + str(self._id) + ' does not have any drawn card')
        
        return self._drawn
    
    def has_card(self) -> bool:
        return self._card is not None
    
    def has_drawn_card(self) -> bool:
        return self._drawn is not None

    def is_protected(self) -> bool:
        return self._is_protected

    def is_eliminated(self) -> bool:
        return self._is_eliminated

    def get_discard(self) -> list[LoveLetterCard]:
        return self._discard
    
    def get_won_rounds(self) -> int:
        return self._won_rounds
    
    def take_card(self, card: LoveLetterCard) -> None:
        if self._drawn:
            raise ValueError("This player already has a drawn card in his hand")
        
        if self._card is None:
            self._card = card
        else:
            self._drawn = card

    def lay_card(self) -> None:
        if self._card is None:
            raise ValueError("The player does not have any card")
        
        self._card = self._drawn
        self._drawn = None
    
    def lay_drawn_card(self) -> None:
        if self._drawn is None:
            raise ValueError("The player does not have any drawn card")
        
        self._drawn = None

    def eliminate(self) -> None:
        self._is_eliminated = True

    def cancel_elimination(self) -> None:
        self._is_eliminated = False

    def protect(self) -> None:
        self._is_protected = True

    def stop_protection(self) -> None:
        self._is_protected = False

    def save_round_won(self):
        self._won_rounds += 1

    def initialize_for_round(self) -> None:
        self._card = None
        self._drawn = None
        self._is_protected = False
        self._is_eliminated = False
        self._discard = []
    
    def add_to_discard(self, card: LoveLetterCard) -> None:
        self._discard.append(card)
    
    def toJson(self):
        card_json = None
        
        if self._card is not None:
            card_json = self._card.toJson()
        
        drawn_card_json = None
        
        if self._drawn is not None:
            drawn_card_json = self._drawn.toJson()
        
        return {
            'id': self._id,
            'card': card_json,
            'drawn_card': drawn_card_json,
            'is_protected': self._is_protected, 
            'id_eliminated': self._is_eliminated,
            'discard': [card.get_character().get_name() for card in self._discard],
            'won_rounds': self._won_rounds,
            'name': self._name
        }
    
