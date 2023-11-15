import GameObjects.Button as B
import GameObjects.Text as T
import GameObject as GO
import Global
import pygame

class Scene():
    gameObjects: GO.GameObject
    selectedGameObject: GO.GameObject # I am making the assumption that the mouse can only be over one button at a time or that the buttons can not overlap
    backgroundColor: pygame.Color
    
    def __init__(self, gameObjects: GO.GameObject, backgroundColor: pygame.Color = pygame.Color('white')) -> None:
        self.gameObjects = gameObjects
        self.backgroundColor = backgroundColor
        self.background = pygame.image.load('background.jpg')
        self.selectedGameObject = None
        
    def draw(self, screen) -> None:
        screen.fill(self.backgroundColor)
        screen.blit(self.background, (0,0))
        for gameObject in self.gameObjects:
            gameObject.draw(screen)
        pygame.display.update()
    
    def processMouseMovement(self, screen)-> None:
        self.selectedGameObject = None
        for gameObject in self.gameObjects:
            if gameObject.processMouseMovement(screen):
                self.selectedGameObject = gameObject
            
    def processMouseClick(self) -> None:
        if self.selectedGameObject != None:
            self.selectedGameObject.processMouseClick()
            
    def processAnyKeyPress(self, screen, keyCode: int) -> bool:
        if self.selectedGameObject != None:
            self.selectedGameObject.processAnyKeyPress(keyCode, screen)