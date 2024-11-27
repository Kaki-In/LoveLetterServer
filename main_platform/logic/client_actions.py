from .table import *

from ..objects.client import *
from ..objects.world import *

import typing as _T
import love_letter as _love_letter
import random as _rd
import json as _json
import asyncio as _asyncio

JOIN_TABLE_ERROR_NO_WAITING_TABLE       = 0
JOIN_TABLE_NO_SUCH_TABLE                = 1
TABLE_ENTER_GAME_CANNOT_ACCEPT_PLAYERS  = 2
TABLE_ENTER_GAME_NO_TABLE_SELECTED      = 3

class ClientActions():
    def __init__(self):
        self._actions: dict[str, _T.Callable[[Client, World], _T.Awaitable]] = {}
        self._sub_actions: dict[str, 'ClientActions'] = {}
    
    def add_action(self, name: str, function: _T.Callable) -> None:
        self._actions[ name ] = function
    
    def add_sub_action(self, name: str, sub_action: 'ClientActions'):
        self._sub_actions[ name ] = sub_action
    
    async def execute_action(self, name: str, args: dict[str, _T.Any], client: Client, world: World):
        if '.' in name:
            p_index = name.index(".")
            prefix = name[:p_index]
            suffix = name[p_index + 1:]
            try:
                await self._sub_actions[prefix].execute_action(suffix, args, client, world)
            except Exception as exc:
                print(exc)
        else:
            try:
                await self._actions[ name ] (client, world, **args)
            except Exception as exc:
                print(exc)
    

class ClientMainActions(ClientActions):
    def __init__(self):
        super().__init__()
        
        self.add_action('join_random_table', self.join_random_table)
        self.add_action('join_named_table', self.join_named_table)
        self.add_action('create_table', self.create_table)
        
        self.add_sub_action('game_action', ClientGameActions())
        self.add_sub_action('table_action', ClientTableActions())
    
    async def join_random_table(self, client: Client, world: World) -> None:
        tables = world.get_tables().get_waiting_tables()
        
        if tables:
            table = _rd.choice(tables)
            
            table.add_ghost(client)
        
        else:
            data = {
                'name': "join_table.error",
                'args': {
                    "code": JOIN_TABLE_ERROR_NO_WAITING_TABLE,
                    "data": {}
                }
            }
            
            client.get_socket().send( _json.dumps(data).encode() )
        
    async def join_named_table(self, client: Client, world: World, name: str) -> None:
        table = world.get_tables().get_table_by_name(name)
        
        if table is None:
            data = {
                'name': "join_table.error",
                'args': {
                    "code": JOIN_TABLE_NO_SUCH_TABLE,
                    "data": {
                        "table_id" : name
                    }
                }
            }
            
            client.get_socket().send( _json.dumps(data).encode() )
        
        else:
            table.add_ghost(client)
    
    async def create_table(self, client: Client, world: World) -> None:
        table_name = world.get_tables().create_table()
        table = world.get_tables().get_table_by_name(table_name)
        
        table.add_ghost(client)
        table.set_ghost_as_player(client)
    

class ClientGameActions(ClientActions):
    def __init__(self):
        super().__init__()
        
        self.add_action('answer_to_interaction', self.answer_to_interaction)
    
    async def answer_to_interaction(self, client: Client, world: World, id: int, answer: dict[str, _T.Any]) -> None:
        game_client = client.get_game_client()
        game_client.resolve_interaction(id, answer)
    

class ClientTableActions(ClientActions):
    def __init__(self):
        super().__init__()
        
        self.add_action('enter_in_game', self.enter_in_game)
        self.add_action('exit_game', self.exit_game)
        self.add_action('start_game', self.start_game)
    
    async def enter_in_game(self, client: Client, world: World) -> None:
        table = world.get_tables().get_table_by_client(client)
        
        logic = TableLogic()
        
        if table:
            if client in table.get_ghosts() and logic.can_accept_players(table):
                table.set_ghost_as_player(client)
            
            else:
                data = {
                    'name': "table.enter_game.error",
                    'args': {
                        "code": TABLE_ENTER_GAME_CANNOT_ACCEPT_PLAYERS,
                        "data": {}
                    }
                }
                
                client.get_socket().send( _json.dumps(data).encode() )
        else:
            data = {
                'name': "table.enter_game.error",
                'args': {
                    "code": TABLE_ENTER_GAME_NO_TABLE_SELECTED,
                    "data": {}
                }
            }
    
    async def exit_game(self, client: Client, world: World) -> None:
        table = world.get_tables().get_table_by_client(client)
        
        logic = TableLogic()
        
        if table:
            if client in table.get_ghosts() and logic.can_loose_players(table):
                table.set_ghost_as_player(client)
            
            else:
                data = {
                    'name': "table.enter_game.error",
                    'args': {
                        "code": TABLE_ENTER_GAME_CANNOT_ACCEPT_PLAYERS,
                        "data": {}
                    }
                }
                
                client.get_socket().send( _json.dumps(data).encode() )
        else:
            data = {
                'name': "table.enter_game.error",
                'args': {
                    "code": TABLE_ENTER_GAME_NO_TABLE_SELECTED,
                    "data": {}
                }
            }
            
            client.get_socket().send( _json.dumps(data).encode() )
    
    async def start_game(self, client: Client, world: World) -> None:
        table = world.get_tables().get_table_by_client(client)
        
        logic = TableLogic()
        
        if table:
            if logic.can_start(table):
                loop = _asyncio.get_event_loop()
                loop.create_task(logic.start(table))
            
            else:
                data = {
                    'name': "table.enter_game.error",
                    'args': {
                        "code": TABLE_ENTER_GAME_CANNOT_ACCEPT_PLAYERS,
                        "data": {}
                    }
                }
                
                client.get_socket().send( _json.dumps(data).encode() )
        else:
            data = {
                'name': "table.enter_game.error",
                'args': {
                    "code": TABLE_ENTER_GAME_NO_TABLE_SELECTED,
                    "data": {}
                }
            }
            
            client.get_socket().send( _json.dumps(data).encode() )
    
    
