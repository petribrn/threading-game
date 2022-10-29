from enum import Enum


class GameModeEnum(Enum):
    easy = {'level': 0, 'time': 60}
    medium = {'level': 1, 'time': 30}
    hardcore = {'level': 2, 'time': 15}


class GameResultEnum(Enum):
    won = 0
    lost = 1
