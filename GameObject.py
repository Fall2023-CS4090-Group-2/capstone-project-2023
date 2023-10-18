import pygame

class GameObject(object):

    def draw(self, screen) -> None:
        pass
    
    def processMouseMovement(self, screen: pygame.Surface) -> bool:
        pass
    
    def processMouseClick(self, screen: pygame.Surface) -> None:
        pass
    
    def processAnyKeyPress(self, screen: pygame.Surface) -> bool:
        pass
