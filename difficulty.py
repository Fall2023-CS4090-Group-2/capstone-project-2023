from enum import Enum


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


enemy_stats = {
    Difficulty.EASY: {
        "speed": 1,
        "max_enemies": 3,
        "damage": 5,
        "score": 5,
        "stop_condition": 5,
    },
    Difficulty.MEDIUM: {
        "speed": 2,
        "max_enemies": 4,
        "damage": 10,
        "score": 8,
        "stop_condition": 10,
    },
    Difficulty.HARD: {
        "speed": 3,
        "max_enemies": 5,
        "damage": 15,
        "score": 10,
        "stop_condition": 15,
    },
}
