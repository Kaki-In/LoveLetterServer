from ..objects import *
from ..rules import *

class LoveLetterCharacterMap():
    def __init__(self, character: LoveLetterCharacter, rule: LoveLetterCharacterRule, count: int):
        self._character: LoveLetterCharacter = character
        self._rule: LoveLetterCharacterRule = rule
        self._count: int = count
    
    def getCharacter(self) -> LoveLetterCharacter:
        return self._character
    
    def getRule(self) -> LoveLetterCharacterRule:
        return self._rule
    
    def getCount(self) -> int:
        return self._count
    

class LoveLetterCharacterMapper():
    def __init__(self):
        self._characters: list[LoveLetterCharacterMap] = []
    
    def addMap(self, map: LoveLetterCharacterMap):
        self._characters.append(map)
    
    def getMapByCharacter(self, character: LoveLetterCharacter):
        for data in self._characters:
            if data.getCharacter() == character:
                return data
    
    def getMapByRule(self, rule: LoveLetterCharacterRule):
        for data in self._characters:
            if data.getRule() == rule:
                return data
    
    def create_default_mapping():
        llmap = LoveLetterCharacterMapper()
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_GUARD, LOVE_LETTER_CHARACTER_GUARD_RULE, 5))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_PRIEST, LOVE_LETTER_CHARACTER_GUARD_RULE, 2))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_BARON, LOVE_LETTER_CHARACTER_GUARD_RULE, 2))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_HANDMAID, LOVE_LETTER_CHARACTER_GUARD_RULE, 2))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_PRINCE, LOVE_LETTER_CHARACTER_GUARD_RULE, 2))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_KING, LOVE_LETTER_CHARACTER_GUARD_RULE, 1))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_COUNTESS, LOVE_LETTER_CHARACTER_GUARD_RULE, 1))
        llmap.addMap(LoveLetterCharacterMapper(LOVE_LETTER_CHARACTER_PRINCESS, LOVE_LETTER_CHARACTER_GUARD_RULE, 2))



