import pygame
import GameObject as GO
import FontConfig as FC

from enum import Enum

class InputFieldState(Enum):
    normal = 0
    hover = 1
    select = 2
    

WHITE: tuple[int] = (255, 255, 255)
BLUE: tuple[int] = (0, 0, 255)
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)

class InputField(GO.GameObject):
    x: int
    y: int 
    fontConfig: FC.FontConfig
    fontSize: int
    width: int
    height: int
    inputText: str
    
    fontObject: pygame.font.Font
    state: InputFieldState
    parameters: list[object]
    
    buttonSurfaceDictionary: dict[int, pygame.Surface]
    
    
    def __init__(self, x: int, y: int, fontConfig: FC.FontConfig, inputText: str = 'Button', width: int = -1, height: int = -1):
        self.x = x
        self.y = y
        self.fontConfig = fontConfig 
        self.inputText = inputText
        self.width = width
        self.height = height
        self.state = InputFieldState.normal   
        self.fontObject = self.fontConfig.makeFontObject()
        self.buttonSurfaceDictionary = {}
        self.buttonSurfaceDictionary[InputFieldState.normal.value] = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.normal.value])
        self.buttonSurfaceDictionary[InputFieldState.select.value]  = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.select.value])
        self.buttonSurfaceDictionary[InputFieldState.hover.value]  = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.hover.value])
        

    def draw(self, screen) -> None:
        updatedRect = screen.blit(self.buttonSurfaceDictionary[self.state.value], (self.x, self.y))
        pygame.display.update(updatedRect)
    
    # returns true if this button is selected
    def processMouseMovement(self, screen: pygame.Surface) -> bool:
        rect: pygame.Rect = self.buttonSurfaceDictionary[self.state.value].get_rect()
        rect.left = self.x
        rect.top = self.y
        isMouseOnButton: bool = rect.collidepoint(pygame.mouse.get_pos())
        if isMouseOnButton:
            if self.state is InputFieldState.normal:
                self.state = InputFieldState.hover
                self.draw(screen)
        if not isMouseOnButton and self.state is InputFieldState.hover:
            self.state = InputFieldState.normal
            self.draw(screen)
        return isMouseOnButton
    
    def processMouseClick(self, screen: pygame.Surface) -> None:
        if self.state == InputFieldState.hover:
            self.state = InputFieldState.select
        else:
            self.state = InputFieldState.normal
    
    def processAnyKeyPress(self, keyCode: int):
        self.inputText += keyCode

