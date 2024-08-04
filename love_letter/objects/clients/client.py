from .message import *
from .result import *

import typing as _T

class LoveLetterClient():
    def __init__(self):
        self._messages_queue: list[LoveLetterClientMessage] = []
        self._interactions_queue: list[LoveLetterClientInteraction] = []
    
    def has_waiting_messages(self) -> bool:
        return len(self._messages_queue) > 0
    
    def pop_message(self) -> LoveLetterClientMessage:
        return self._messages_queue.pop(0)
    
    def has_waiting_interactions(self) -> bool:
        return len(self._interactions_queue) > 0
    
    def get_next_waiting_interaction(self) -> LoveLetterClientInteraction:
        if len(self._interactions_queue) == 0:
            raise TypeError("there is no interaction yet")
        
        return self._interactions_queue[0]
    
    def send_message(self, message: LoveLetterClientMessage) -> None:
        self._messages_queue.append(message)
    
    def interact(self, interaction: LoveLetterClientInteraction) -> None:
        self._interactions_queue.append(interaction)
    
