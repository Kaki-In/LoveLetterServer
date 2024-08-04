import love_letter as _love_letter
import promisio as _promisio
import typing as _T

class DistantClient(_love_letter.LoveLetterClient):
    def __init__(self):
        super().__init__()
        
        self._messages: list[_love_letter.ClientMessage] = []
        self._interactions: list[tuple[int, _love_letter.ClientMessage, _T.Any]] = []
        
        self._began_interactions: list[tuple[int, _love_letter.ClientMessage, _T.Any]] = []
        
        self._last_interact_id = 0
    
    async def send_message(self, message: _love_letter.ClientMessage) -> None:
        self._messages.append(message)
    
    def get_new_interact_id(self) -> int:
        self._last_interact_id += 1
        return self._last_interact_id
    
    async def interact(self, message: _love_letter.ClientMessage) -> _love_letter.ClientResult:
        def func(resolver, rejecter):
            self._interactions.append((self.get_new_interact_id(), message, resolver))
        
        while True:
            promise: _promisio.Promise =_promisio.Promise(func)
            
            result: _love_letter.ClientResult = await promise
            
            if result.get_name() == message.get_name():
                return result
    
    def messages_are_waiting(self) -> bool:
        return bool(self._messages)
    
    def interactions_are_waiting(self) -> bool:
        return bool(self._interactions)
    
    def get_next_message(self) -> _love_letter.ClientMessage:
        return self._messages.pop(0)
    
    def get_next_interaction(self) -> tuple[int, _love_letter.ClientMessage]:
        interaction = self._interactions.pop(0)
        
        self._began_interactions.append(interaction)
        
        return interaction[:2]
    
    def resolve_interaction(self, id: int, result: dict[str, _T.Any]) -> None:
        for began_interaction in self._began_interactions:
            if began_interaction[0] == id:
                self._began_interactions.remove(began_interaction)
                
                client_result = _love_letter.ClientResult(began_interaction[1].get_name(), result)
                
                began_interaction[2] (client_result)
                return
        
        raise ReferenceError("no such began interaction was found")
    
