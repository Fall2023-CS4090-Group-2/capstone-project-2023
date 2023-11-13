import pygame
from enum import Enum


class GameObject(object):

    def draw(self, screen) -> None:
        pass
    
    def processMouseMovement(self, screen) -> bool:
        pass
    
    def processMouseClick(self) -> None:
        pass
    
    def processAnyKeyPress(self, screen, keyCode: int) -> bool:
        pass

    def changeState(self, newState: Enum) -> None:
        pass