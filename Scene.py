import GameObjects.Button as B
import GameObjects.Text as T
import GameObject as GO
import pygame

class Scene():
    gameObjects: GO.GameObject
    
    selectedGameObject: GO.GameObject # I am making the assumption that the mouse can only be over one button at a time or that the buttons can not overlap
    
    def __init__(self, gameObjects: GO.GameObject) -> None:
        self.gameObjects = gameObjects
        
    def draw(self, screen: pygame.Surface) -> None:
        for gameObject in self.gameObjects:
            gameObject.draw(screen)
    
    def processMouseMovement(self, screen: pygame.Surface) -> None:
        for gameObject in self.gameObjects:
            if gameObject.processMouseMovement(screen):
                self.selectedGameObject = gameObject
            
    def processMouseClick(self) -> None:
        self.selectedGameObject.processMouseClick()