import love_letter as _love_letter
import typing as _T

import board_game as _board_game

class DistantClient(_board_game.BoardGameClient):
    def __init__(self):
        _board_game.BoardGameClient.__init__(self)
        
        self._messages: list[_board_game.BoardGameClientMessage] = []
        self._interactions: list[tuple[int, _board_game.BoardGameClientMessage, _T.Any]] = []
        
        self._began_interactions: list[tuple[int, _board_game.BoardGameClientMessage, _T.Any]] = []
        
        self._last_interact_id = 0
    
    def send_message(self, message: _board_game.BoardGameClientMessage) -> None:
        self._messages.append(message)
    
    def get_new_interact_id(self) -> int:
        self._last_interact_id += 1
        return self._last_interact_id
    
    def interact(self, interaction: _board_game.BoardGameClientMessage) -> None:
        def func(resolver, rejecter):
            self._interactions.append((self.get_new_interact_id(), interaction, resolver))
            
    def messages_are_waiting(self) -> bool:
        return bool(self._messages)
    
    def interactions_are_waiting(self) -> bool:
        return bool(self._interactions)
    
    def get_next_message(self) -> _board_game.BoardGameClientMessage:
        return self._messages.pop(0)
    
    def get_next_interaction(self) -> tuple[int, _board_game.BoardGameClientMessage]:
        interaction = self._interactions.pop(0)
        
        self._began_interactions.append(interaction)
        
        return interaction[:2]
    
#    def resolve_interaction(self, id: int, result: dict[str, _T.Any]) -> None:
#        for began_interaction in self._began_interactions:
#            if began_interaction[0] == id:
#                self._began_interactions.remove(began_interaction)
#                
#                client_result = _board_game.BoardGameClientResponse(began_interaction[1].get_name(), result)
#                
#                began_interaction[2] (client_result)
#                return
#        
#        raise ReferenceError("no such began interaction was found")
    
