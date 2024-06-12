from ..objects.table import *
from ..controllers import *

import love_letter as _love_letter

class TableLogic():
    def __init__(self):
        pass
    
    async def start(self, table: Table, clients: list[DistantClient]) -> None:
        if not self.can_start(table):
            raise ValueError("impossible to start this table")
        
        table.set_state(TABLE_STATE_STARTING)
        
        players: list[_love_letter.LoveLetterPlayer] = []
        notifier = _love_letter.LoveLetterNotifier()
        
        for id, client in enumerate(clients):
            player = _love_letter.LoveLetterPlayer(id)
            players.append( player )
            notifier.plug_client_with_player(client, player)
        
        try:
            game = _love_letter.LoveLetterGame( *players )
        except Exception as exc:
            table.set_state(TABLE_STATE_WAITING)
            return
        
        mapper = _love_letter.LoveLetterCharacterMapper.create_default_mapping()
        
        rule = _love_letter.LoveLetterGameRules(notifier, mapper)
        
        table.set_game(game)
        table.set_state(TABLE_STATE_PLAYING)
        
        try:
            await rule.main_game(game)
        except Exception as exc:
            reason = _love_letter.ClientReason(_love_letter.LOVE_LETTER_GAME_CRASHED, {
                'error': str(exc)
            })
            
            await notifier.cancel_game(reason)
            table.set_state( TABLE_STATE_GAVE_UP )
            
            raise
        else:
            table.set_state( TABLE_STATE_FINISHED )
    
    def can_start(self, table: Table) -> bool:
        return len(table.get_players()) >= 2 and table.get_state() == TABLE_STATE_WAITING
    

