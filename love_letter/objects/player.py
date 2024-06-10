from .card import LoveLetterCard
import events as _events

PLAYER_EVENT_CARDS = 0
PLAYER_EVENT_PROTECTION = 1
PLAYER_EVENT_ELIMINATION = 2
PLAYER_EVENT_DISCARD = 3
PLAYER_EVENT_ROUND_WON = 4
PLAYER_EVENT_INITIALIZATION = 5

class LoveLetterPlayer:
    def __init__(self, player_id: int):
        self._id: int = player_id
        self._card: LoveLetterCard | None = None
        self._drawn: LoveLetterCard | None = None
        self._is_protected: bool = False
        self._is_eliminated: bool = False
        self._discard: list[LoveLetterCard] = []
        self._won_rounds: int = 0
        
        self._events: _events.EventObject = _events.EventObject(
            PLAYER_EVENT_CARDS,
            PLAYER_EVENT_DISCARD,
            PLAYER_EVENT_ELIMINATION,
            PLAYER_EVENT_PROTECTION,
            PLAYER_EVENT_ROUND_WON,
            PLAYER_EVENT_INITIALIZATION
        )

    def get_id(self) -> int:
        return self._id

    def get_card(self) -> LoveLetterCard | None:
        return self._card

    def get_drawn_card(self) -> LoveLetterCard | None:
        return self._drawn

    def is_protected(self) -> bool:
        return self._is_protected

    def is_eliminated(self) -> bool:
        return self._is_eliminated

    def get_discard(self) -> list[LoveLetterCard]:
        return self._discard

    def take_card(self, card: LoveLetterCard) -> None:
        if self._drawn:
            raise ValueError("This player already has a drawn card in his hand")
        
        self._drawn = card
        self._events[PLAYER_EVENT_CARDS].emit(self._drawn, self._card)

    def lay_card(self) -> None:
        if self._card is None:
            raise ValueError("The player does not have any card")
        
        self._discard.append(self._card)
        self._card = self._drawn
        self._drawn = None
        self._events[PLAYER_EVENT_CARDS].emit(self._drawn, self._card)

    def lay_drawn_card(self) -> None:
        if self._drawn is None:
            raise ValueError("The player does not have any drawn card")
        
        self._discard.append(self._drawn)
        self._drawn = None
        self._events[PLAYER_EVENT_CARDS].emit(self._drawn, self._card)

    def eliminate(self) -> None:
        self._is_eliminated = True
        self._events[PLAYER_EVENT_ELIMINATION].emit(True)

    def cancel_elimination(self) -> None:
        self._is_eliminated = False
        self._events[PLAYER_EVENT_ELIMINATION].emit(False)

    def protect(self) -> None:
        self._is_protected = True
        self._events[PLAYER_EVENT_PROTECTION].emit(True)

    def stop_protection(self) -> None:
        self._is_protected = False
        self._events[PLAYER_EVENT_PROTECTION].emit(False)

    def save_round_won(self):
        self._won_rounds += 1
        self._events[PLAYER_EVENT_ROUND_WON].emit(self._won_rounds)

    def initialize_for_round(self) -> None:
        self._card = None
        self._drawn = None
        self._is_protected = False
        self._is_eliminated = False
        self._discard = []
        
        self._events[PLAYER_EVENT_INITIALIZATION].emit()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
