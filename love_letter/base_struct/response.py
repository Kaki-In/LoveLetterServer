import board_game as _board_game

class LoveLetterClientResponse(_board_game.BoardGameClientResponse):
    def __init__(self, name: str, args: dict):
        super().__init__(name, args)

