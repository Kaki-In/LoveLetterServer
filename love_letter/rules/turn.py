from love_letter.rules.result import LoveLetterResult
from .rule import *
from .task import *

from ..objects.context import *

class LoveLetterTurnRule(LoveLetterRule):
    def __init__(self):
        super().__init__()

    def should_be_played_again(self, context: LoveLetterGameContext, results: tuple[LoveLetterResult, LoveLetterResult, LoveLetterResult, LoveLetterResult]) -> bool:
        return False

    def get_next_tasks(self, context: LoveLetterGameContext) -> list[LoveLetterTask]:
        state = context.get_state()
        round_state = state.get_round_state().get_turn_state()
        player = round_state.get_player()

        return [
            LoveLetterDrawCardTask(player),
            LoveLetterChooseCardTask(player),
            LoveLetterDiscardTask(player, round_state.get_chosen_card(), LOVE_LETTER_DISCARD_REASON.PLAY),
            LoveLetterPlayCharacterTask(player, round_state.get_character())
        ]


