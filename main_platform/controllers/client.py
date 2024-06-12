import love_letter as _love_letter
import events as _events
import promisio as _promisio

DISTANT_CLIENT_EVENT_MESSAGE_CAME       = 0
DISTANT_CLIENT_EVENT_INTERACTION_NEEDED = 1

class DistantClient(_love_letter.LoveLetterClient):
    def __init__(self):
        super().__init__()
        
        self._events = _events.EventObject(
            DISTANT_CLIENT_EVENT_INTERACTION_NEEDED,
            DISTANT_CLIENT_EVENT_MESSAGE_CAME
        )
        
        self._resolve = None
    
    async def send_message(self, message: _love_letter.ClientMessage) -> None:
        self._events[ DISTANT_CLIENT_EVENT_MESSAGE_CAME ].emit(message)
    
    async def interact(self, message: _love_letter.ClientMessage) -> _love_letter.ClientResult:
        def func(resolver, rejecter):
            self._resolve = resolver
        
        
        while True:
            promise: _promisio.Promise =_promisio.Promise(func)
            self._events[ DISTANT_CLIENT_EVENT_INTERACTION_NEEDED ].emit(message, promise)
            
            result: _love_letter.ClientResult = await promise
            if result.get_name() == message.get_name():
                return result
    
