"""
from ..objects.context.board.deck.card.character import *
from ..objects.context.rules.game.round.player.character_play import *
from ..objects.context.rules.game.round.player.character_discard import *

import typing as _T

class LoveLetterCharacterMap():
    def __init__(self, character: LoveLetterCharacter, rule: LoveLetterCharacterTask, discard_rule: LoveLetterCharacterDiscardTask, count: int):
        self._character: LoveLetterCharacter = character
        self._rule = rule
        self._discard_rule = discard_rule
        self._count: int = count
    
    def get_character(self) -> LoveLetterCharacter:
        return self._character
    
    def get_rule(self) -> LoveLetterCharacterTask:
        return self._rule
    
    def get_count(self) -> int:
        return self._count

class LoveLetterCharacterMapper():
    def __init__(self):
        self._characters: list[LoveLetterCharacterMap] = []
    
    def add_map(self, map: LoveLetterCharacterMap):
        self._characters.append(map)
    
    def get_map_by_character(self, character: LoveLetterCharacter) -> LoveLetterCharacterMap:
        for data in self._characters:
            if data.get_character() == character:
                return data
        
        raise KeyError('no such map')
    
    def get_map_by_rule(self, rule: LoveLetterCharacterRule) -> LoveLetterCharacterMap:
        for data in self._characters:
            if data.get_rule() == rule:
                return data
        
        raise KeyError('no such map')
    
    def get_map_by_character_name(self, name: str) -> LoveLetterCharacterMap:
        for data in self._characters:
            if data.get_character().get_name() == name:
                return data
        
        raise KeyError('no such map')
    
    def get_all_maps(self) -> list[LoveLetterCharacterMap]:
        return self._characters
    
def create_default_characters_mapping() -> LoveLetterCharacterMapper:
    llmap = LoveLetterCharacterMapper()
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_GUARD, LoveLetterGuardRule(), 5))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_PRIEST, LoveLetterPriestRule(), 2))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_BARON, LoveLetterBaronRule(), 2))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_HANDMAID, LoveLetterHandMaidRule(), 2))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_PRINCE, LoveLetterPrinceRule(), 2))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_KING, LoveLetterKingRule(), 1))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_COUNTESS, LoveLetterCountessRule(), 1))
    llmap.add_map(LoveLetterCharacterMap(LOVE_LETTER_CHARACTER_PRINCESS, LoveLetterPrincessRule(), 1))
    
    return llmap


"""