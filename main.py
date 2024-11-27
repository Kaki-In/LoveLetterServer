#!/usr/bin/python3

# from main_platform import *
from love_letter import *
from love_letter.mapping.rules_map import *
import sys
import json
import asyncio
import ssl as _ssl

from board_game import *

class LocalClient(BoardGameClient):
    def __init__(self):
        super().__init__()
    
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

    deck = LoveLetterDeck()

    c = LoveLetterConfiguration(charc, roundsc, gamec)

    context = LoveLetterGameContext(
        LoveLetterBoard(
            players, deck
        ),
        LoveLetterGameState(),
        c
    )

    protocols = LoveLetterRuleMap()

    game_handler = BoardGameHandler(context, protocols)
    game_handler.add_main_task(LoveLetterPlayGameTask())

    actions = []

    import time
    while not game_handler.is_terminated():
        time.sleep(5)
        new_actions = game_handler.main_once()
        actions += new_actions

        print("Resulting actions :", new_actions)

        if game_handler.requires_interaction():
            print("An interaction is required!!!")
            interaction = game_handler.get_required_interaction()
            print(interaction, interaction.toJson())

            player: int = interaction.get_args()['player']

            game_handler.answer(LoveLetterChoosePlayerResponse(player2))


        print("-----------------------------")

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

