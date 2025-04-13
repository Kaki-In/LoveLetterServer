from board_game.base_struct.message import *
from board_game.base_struct.response import *
from board_game.base_struct.interaction import *

import typing as _T

class BoardGameClient():
    """
    This class defines a client of the Board Game. 
    """

    def __init__(self):
        self._messages_queue: list[BoardGameClientMessage] = []
        self._interactions_queue: list[BoardGameClientInteraction] = []
    
    def has_waiting_messages(self) -> bool:
        """
        Returns True if the client receveid messages.  
        """
        return len(self._messages_queue) > 0
    
    def pop_message(self) -> BoardGameClientMessage:
        """
        Returns the oldest sent message to the client. 
        """
        return self._messages_queue.pop(0)
    
    def has_waiting_interactions(self) -> bool:
        """
        Returns True if the client received interactions. 
        """
        return len(self._interactions_queue) > 0
    
    def get_next_waiting_interaction(self) -> BoardGameClientInteraction:
        """
        Returns the oldest interaction that has not been answered. 
        """
        if len(self._interactions_queue) == 0:
            raise TypeError("there is no interaction yet")
        
        return self._interactions_queue[0]
    
    def send_message(self, message: BoardGameClientMessage) -> None:
        """
        Sends a message to the client. 
        """
        self._messages_queue.append(message)
    
    def interact(self, interaction: BoardGameClientInteraction) -> None:
        """
        Sends an interaction to the client. 
        """
        self._interactions_queue.append(interaction)
    
