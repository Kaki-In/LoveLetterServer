#!/usr/bin/python3

import sys
sys.dont_write_bytecode = True

#from main_platform import *
from love_letter import *
from love_letter.mapping.rules_map import *
import json
import asyncio
import ssl as _ssl

from board_game import *


class LocalClient(BoardGameClient):
    def __init__(self):
        BoardGameClient.__init__(self)
    
    def send_message(self, message: BoardGameClientMessage) -> None:
        print("-------------------------------------------")
        print("Received message for client", id(self), ":")
        print(message.toJson())
        print("-------------------------------------------")
    
    def interact(self, message: BoardGameClientInteraction) -> BoardGameClientResponse:
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
        
        return BoardGameClientResponse(result["name"], result["args"])

async def test(args):
    client1 = LocalClient()
    client2 = LocalClient()

    player1 = LoveLetterPlayer(0, "Bob")
    player2 = LoveLetterPlayer(1, "Bill")
    player3 = LoveLetterPlayer(2, "Boule")

    players = [player1, player2, player3]

    charc = LOVE_LETTER_CHARACTER_CONFIGURATION_DEFAULT

    roundsc = LoveLetterRoundsConfiguration(
        LOVE_LETTER_ROUNDS_EQUALITY_POLICY.RANDOM
    )

    gamec = LoveLetterGameConfiguration(
        None
    )

    c = LoveLetterConfiguration(charc, roundsc, gamec)

    deck = LoveLetterDeck()
    board = LoveLetterBoard([player1, player2, player3], deck)

    context = LoveLetterContext(c, board)

    protocols = LoveLetterRuleMap()

    game_handler = BoardGameHandler(context, protocols)
    game_handler.add_main_task(LoveLetterPlayGameTask(c, board))

    actions = []

    import time
    while not game_handler.is_terminated():
        new_actions = game_handler.main_once()
        actions += new_actions

        print("Resulting actions :", new_actions)

        if game_handler.requires_interaction():
            print("An interaction is required!!!")
            interaction = game_handler.get_required_interaction()
            print(interaction, interaction.toJson())

            if type(interaction) == LoveLetterChooseCardInteraction:
                json_result = "HAND_CARD"
                response = interaction.json_to_response(json_result, context)
            
            elif type(interaction) == LoveLetterChoosePlayerInteraction:
                json_result = {
                    'player': 0
                }
                response = interaction.json_to_response(json_result, context)

            elif type(interaction) == LoveLetterChooseCharacterInteraction:
                json_result = {
                    'player': 0
                }
                response = interaction.json_to_response(json_result, context)
            else:
                response = None

            game_handler.answer(response)


        print("-----------------------------")
        time.sleep(2)

    return 0

async def main(args):
    return await test(args)

    world = World()
    server = Server("localhost", 40000, _ssl._create_unverified_context(), ssl = False)
    
    logic = ServerLogic()
    
    await logic.main(server, world)
    
    return 0

if __name__ == "__main__":
    sys.exit(asyncio.run(main(sys.argv)))

