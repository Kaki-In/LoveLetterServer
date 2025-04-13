import enum as _enum

class BOARD_GAME_RULE_STATE(_enum.IntEnum):
    """
    This enumeration describes the states of a task execution. 

    STATE_IDLE: the executor does not run a task (start or end). 
    STATE_STARTING: the executor is launching the starting phase of a task
    STATE_RUNNING: the executor is launching the main phase of a task
    STATE_WAITING: the executor is waiting for an interaction answer
    STATE_ENDING: the executor is launching the ending phase of a task
    """
    
    STATE_IDLE      = 0
    STATE_STARTING  = 1
    STATE_RUNNING   = 2
    STATE_WAITING   = 3
    STATE_ENDING    = 4

