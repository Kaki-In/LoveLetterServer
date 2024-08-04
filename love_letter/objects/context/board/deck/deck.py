from .card import *

import random as _random
import events as _events

DECK_EVENT_NUMBER_CHANGED = 0

class LoveLetterDeck():
    def __init__(self):
        self._cards: list[ LoveLetterCard ] = []
        self._events: _events.EventObject = _events.EventObject(
            DECK_EVENT_NUMBER_CHANGED
        )

        self._hidden_card: LoveLetterCard | None = None
        self._removed_cards: list[LoveLetterCard] = []
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def add_card(self, card) -> None:
        self._cards.append(card)
        
        self._events[ DECK_EVENT_NUMBER_CHANGED ].emit(card)
        
    def shuffle(self) -> None:
        _random.shuffle(self._cards)
    
    def get_hidden_card(self) -> LoveLetterCard:
        if self._hidden_card is None:
            raise ValueError('there is no hidden card at this time')

        return self._hidden_card
    
    def set_hidden_card(self, card: LoveLetterCard) -> None:
        self._hidden_card = card
    
    def has_hidden_card(self) -> bool:
        return self._hidden_card is not None

    def get_removed_cards(self) -> tuple[LoveLetterCard, ...]:
        return tuple(self._removed_cards)
    
    def add_removed_card(self, card: LoveLetterCard) -> None:
        self._removed_cards.append(card)
    
    def take_card(self) -> LoveLetterCard:
        if self._cards:
            card = self._cards.pop()
        
            self._events[ DECK_EVENT_NUMBER_CHANGED ].emit(card)
        elif self._hidden_card is not None:
            card = self._hidden_card

        else:
            raise ValueError("there is no card in this deck")
        
        return card
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def toJson(self):
        return {
            'cards': [card.toJson() for card in self._cards],
            'removed_cards': [card.toJson() for card in self._removed_cards],
            'hidden_card': self._hidden_card is None
        }
    
