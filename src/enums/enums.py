from enum import Enum


class GameModeEnum(Enum):
    easy = {'level': 0, 'countdown': 30, 'time_to_move': 1.2}
    medium = {'level': 1, 'countdown': 20, 'time_to_move': 1}
    hardcore = {'level': 2, 'countdown': 10, 'time_to_move': 0.65}
