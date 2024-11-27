from ..objects.table import *
from ..objects.client import *
from ..controllers import *

import love_letter as _love_letter

class TableLogic():
    def __init__(self):
        pass
    
    def set_table_state(self, table: Table, state: int) -> None:
        table.set_state(state)
        
        if state in (TABLE_STATE_FINISHED, TABLE_STATE_GAVE_UP):
            for player in table.get_players():
                table.set_player_as_ghost(player)
    
    async def start(self, table: Table) -> None:
        raise NotImplementedError()
#        if not self.can_start(table):
#            raise ValueError("impossible to start this table")
#        
#        clients = table.get_players()
#        
#        self.set_table_state(table, TABLE_STATE_STARTING)
#        
#        players: list[_love_letter.LoveLetterPlayer] = []
#        notifier = _love_letter.LoveLetterNotifier()
#        
#        for id, client in enumerate(clients):
#            player = _love_letter.LoveLetterPlayer(id, client.get_name())
#            players.append( player )
#            notifier.plug_client_with_player(client.get_game_client(), player)
#        
#        try:
#            game = _love_letter.LoveLetterTable( *players )
#        except Exception as exc:
#            self.set_table_state(table, TABLE_STATE_WAITING)
#            return
#        
#        mapper = _love_letter.LoveLetterCharacterMapper.create_default_mapping()
#        
#        rule = _love_letter.LoveLetterGameRules(notifier, mapper)
#        
#        table.set_game(game)
#        self.set_table_state(table, TABLE_STATE_PLAYING)
#        
#        notifier.plug_to_game(game)
#        
#        try:
#            await rule.main_game(game)
#        except Exception as exc:
#            reason = _love_letter.ClientReason(_love_letter.LOVE_LETTER_GAME_CRASHED, {
#                'error': str(exc)
#            })
#            
#            print("An error occured while handling the game")
#            
#            await notifier.cancel_game(reason)
#            self.set_table_state(table, TABLE_STATE_GAVE_UP )
#            
#            raise
#        else:
#            self.set_table_state(table, TABLE_STATE_FINISHED )
#    
    def can_accept_players(self, table: Table) -> bool:
        return len(table.get_players()) < 4 and table.get_state() == TABLE_STATE_WAITING
    
    def can_loose_players(self, table: Table) -> bool:
        return table.get_state() == TABLE_STATE_WAITING
    
    def can_start(self, table: Table) -> bool:
        return 2 <= len(table.get_players()) <= 4 and table.get_state() == TABLE_STATE_WAITING
    

