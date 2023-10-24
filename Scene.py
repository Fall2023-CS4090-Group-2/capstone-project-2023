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
        
    def draw(self) -> None:
        Global.GAME_SCREEN.fill(self.backgroundColor)
        for gameObject in self.gameObjects:
            gameObject.draw()
        pygame.display.update()
    
    def processMouseMovement(self) -> None:
        self.selectedGameObject = None
        for gameObject in self.gameObjects:
            if gameObject.processMouseMovement():
                self.selectedGameObject = gameObject
            
    def processMouseClick(self) -> None:
        print("processing mouse click")
        print(self.selectedGameObject)
        if self.selectedGameObject != None:
            self.selectedGameObject.processMouseClick()
            
    def processAnyKeyPress(self, keyCode: int) -> bool:
        if self.selectedGameObject != None:
            self.selectedGameObject.processAnyKeyPress(keyCode)