#!/usr/bin/python3

from main_platform import *
from love_letter import *
import sys
import json
import asyncio

class LocalClient(LoveLetterClient):
    def __init__(self):
        super().__init__()
    
    async def send_message(self, message: ClientMessage) -> None:
        print("-------------------------------------------")
        print("Received message for client", id(self), ":")
        print(message.toJson())
        print("-------------------------------------------")
    
    async def interact(self, message: ClientMessage) -> ClientResult:
        print("-------------------------------------------")
        print("Received message for client", id(self), ":")
        print(message.toJson())
        print("-------------------------------------------")
        
        while True:
            try:
                result = json.loads(input("Waiting for an answer : "))
            except Exception:
                print("Cette syntax ne semble pas correct...")
            else:
                break
        
        return ClientResult(result["name"], result["args"])

async def main(args):
    client1 = LocalClient()
    client2 = LocalClient()
    
    player1 = LoveLetterPlayer(0)
    player2 = LoveLetterPlayer(1)
    
    notifier = LoveLetterNotifier()
    notifier.plug_client_with_player(client1, player1)
    notifier.plug_client_with_player(client2, player2)
    
    mapper = LoveLetterCharacterMapper.create_default_mapping()
    
    game = LoveLetterGame(player1, player2)
    
    rule = LoveLetterGameRules(notifier, mapper)
    
    await rule.main_game(game)
    
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main(sys.argv)))
