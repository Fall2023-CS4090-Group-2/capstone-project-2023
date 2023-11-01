import pygame
import GameObject as GO
import FontConfig as FC
import Global

from enum import Enum

class ButtonState(Enum):
    normal = 0
    hover = 1
    press = 2

WHITE: tuple[int] = (255, 255, 255)
BLUE: tuple[int] = (0, 0, 255)
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)

class Button(GO.GameObject):
    x: int
    y: int 
    fontConfig: FC.FontConfig
    fontSize: int
    width: int
    height: int
    buttonText: str
    
    fontObject: pygame.font.Font
    state: ButtonState
    parameters: list[object]
    
    buttonSurfaceDictionary: dict[int, pygame.Surface]
    
    
    def __init__(self, x: int, y: int, fontConfig: FC.FontConfig, buttonText: str = 'Button', width: int = -1, height: int = -1, onClickFunction = lambda: print("Default Button Function"), parameters: list[object] = None):
        self.x = x
        self.y = y
        self.fontConfig = fontConfig 
        self.buttonText = buttonText
        self.width = width
        self.height = height
        self.state = ButtonState.normal   
        self.fontObject = self.fontConfig.makeFontObject()
        self.onClickFunction = onClickFunction 
        self.parameters = parameters
        self.buttonSurfaceDictionary = {}
        self.buttonSurfaceDictionary[ButtonState.normal.value] = self.fontObject.render(self.buttonText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[ButtonState.normal.value])
        self.buttonSurfaceDictionary[ButtonState.press.value]  = self.fontObject.render(self.buttonText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[ButtonState.press.value])
        self.buttonSurfaceDictionary[ButtonState.hover.value]  = self.fontObject.render(self.buttonText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[ButtonState.hover.value])
        

    def draw(self) -> None:
        updatedRect = Global.GAME_SCREEN.blit(self.buttonSurfaceDictionary[self.state.value], (self.x, self.y))
        pygame.display.update(updatedRect)
    
    # returns true if this button is selected
    def processMouseMovement(self) -> bool:
        rect: pygame.Rect = self.buttonSurfaceDictionary[self.state.value].get_rect()
        rect.left = self.x
        rect.top = self.y
        isMouseOnButton: bool = rect.collidepoint(pygame.mouse.get_pos())
        if isMouseOnButton:
            if self.state is ButtonState.normal:
                self.state = ButtonState.hover
                self.draw()
        if not isMouseOnButton and self.state is ButtonState.hover:
            self.state = ButtonState.normal
            self.draw()
        return isMouseOnButton
    
    def processMouseClick(self) -> None:
        if self.parameters is None:
            self.onClickFunction()
        else:
            self.onClickFunction(self.parameters)

