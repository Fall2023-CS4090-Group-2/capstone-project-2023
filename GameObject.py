import pygame
from enum import Enum


class GameObject(object):

    def draw(self) -> None:
        pass
    
    def processMouseMovement(self) -> bool:
        pass
    
    def processMouseClick(self) -> None:
        pass
    
    def processAnyKeyPress(self, keyCode: int) -> bool:
        pass

    def changeState(self, newState: Enum) -> None:
        pass