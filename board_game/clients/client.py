from board_game.base_struct.message import *
from board_game.base_struct.response import *
from board_game.base_struct.interaction import *

import typing as _T

class BoardGameClient():
    def __init__(self):
        self._messages_queue: list[BoardGameClientMessage] = []
        self._interactions_queue: list[BoardGameClientInteraction] = []
    
    def has_waiting_messages(self) -> bool:
        return len(self._messages_queue) > 0
    
    def pop_message(self) -> BoardGameClientMessage:
        return self._messages_queue.pop(0)
    
    def has_waiting_interactions(self) -> bool:
        return len(self._interactions_queue) > 0
    
    def get_next_waiting_interaction(self) -> BoardGameClientInteraction:
        if len(self._interactions_queue) == 0:
            raise TypeError("there is no interaction yet")
        
        return self._interactions_queue[0]
    
    def send_message(self, message: BoardGameClientMessage) -> None:
        self._messages_queue.append(message)
    
    def interact(self, interaction: BoardGameClientInteraction) -> None:
        self._interactions_queue.append(interaction)
    
