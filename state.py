from enum import Enum


class State(Enum):
    MAIN_MENU = 0
    RUNNING = 1
    PAUSED = 2
    EXIT = 3
    MAIN_MUSIC = 4
    PAUSE_MUSIC = 5
