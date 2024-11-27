import enum as _enum

class BOARD_GAME_RULE_STATE(_enum.IntEnum):
    STATE_IDLE      = 0
    STATE_STARTING  = 1
    STATE_RUNNING   = 2
    STATE_WAITING   = 3
    STATE_ENDING    = 4

