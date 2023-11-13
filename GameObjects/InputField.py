import pygame
import GameObject as GO
import FontConfig as FC
import Global 

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
        

    def draw(self, screen)-> None:
        updatedRect = screen.blit(self.buttonSurfaceDictionary[self.state.value], (self.x, self.y))
        pygame.display.update(updatedRect)
    
    def changeState(self, newState: Enum) -> None:
        self.state = newState
        self.draw()
        
    
    # returns true if this button is selected
    def processMouseMovement(self) -> bool:
        rect: pygame.Rect = self.buttonSurfaceDictionary[self.state.value].get_rect()
        rect.left = self.x
        rect.top = self.y
        isMouseOnInputField: bool = rect.collidepoint(pygame.mouse.get_pos())
        if self.state == InputFieldState.select:
            return True
        elif self.state == InputFieldState.normal:
            if isMouseOnInputField:
                self.changeState(InputFieldState.hover)
        elif self.state == InputFieldState.hover:
            if not isMouseOnInputField:
                self.changeState(InputFieldState.normal)
        return isMouseOnInputField
    
    def processMouseClick(self) -> None:
        if self.state == InputFieldState.hover:
            self.changeState(InputFieldState.select)
        elif self.state == InputFieldState.select:
            self.changeState(InputFieldState.normal)
            
    
    def processAnyKeyPress(self, screen, keyCode: int):
        if keyCode == pygame.K_BACKSPACE:
            self.inputText = self.inputText[:-1]
        elif keyCode == pygame.K_SPACE:
            self.inputText += " "
        else:
            self.inputText += pygame.key.name(keyCode)
        self.updateButtonSurfaceDictionary()
        self.draw(screen)
        
    def updateButtonSurfaceDictionary(self) -> None:
        self.buttonSurfaceDictionary[InputFieldState.normal.value] = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.normal.value])
        self.buttonSurfaceDictionary[InputFieldState.select.value]  = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.select.value])
        self.buttonSurfaceDictionary[InputFieldState.hover.value]  = self.fontObject.render(self.inputText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[InputFieldState.hover.value])
