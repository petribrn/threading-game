from enum import Enum


class GameModeEnum(Enum):
    easy = {'level': 0, 'countdown': 30, 'time_to_move': 1.5}
    medium = {'level': 1, 'countdown': 20, 'time_to_move': 1}
    hardcore = {'level': 2, 'countdown': 5, 'time_to_move': 0.5}


class GameResultEnum(Enum):
    won = 0
    lost = 1
