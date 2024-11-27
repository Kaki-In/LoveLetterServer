import board_game as _board_game

class LoveLetterClientInteraction(_board_game.BoardGameClientInteraction):
    def __init__(self, name: str, args: dict):
        super().__init__(name, args)

