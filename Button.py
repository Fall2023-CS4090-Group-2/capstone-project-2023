import pygame
import FontConfig as FC

WHITE: tuple[int] = (255, 255, 255)
BLUE: tuple[int] = (0, 0, 255)
RED: tuple[int] = (255, 0, 0)
GREEN: tuple[int] = (0, 255, 0)

class Button():
    fontObject: pygame.font.Font
    x: int
    y: int 
    fontConfig: FC.FontConfig
    fontSize: int
    width: int
    height: int
    buttonText: str
    onePress: bool
    buttonSurface: pygame.Surface
    
    def __init__(self, x: int, y: int, fontConfig: FC.FontConfig, buttonText: str = 'Button', width: int = -1, height: int = -1, onclickFunction = None, onePress: bool = False):
        self.fontObject = fontConfig.makeFontObject()
        self.fontConfig = fontConfig 
        self.x = x
        self.y = y
        self.buttonText = buttonText
        # self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.width = width
        self.height = height
        if self.width == -1:
            self.width = self.fontObject.size(buttonText)[0] + fontConfig.size / 2
        if self.height == -1:
            self.height = self.fontObject.size(buttonText)[1]        
            
        self.buttonSurface = pygame.Surface((self.width, self.height))
            
        
        self.fillColors = {                               
            'normal': '#000000',
            'hover': '#000111',
            'pressed': '#111111',
        }
        
    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        text = self.fontObject.render(self.buttonText, True, self.fontConfig.textColor, self.fontConfig.buttonColor)
        textRect = text.get_rect()
        screen.blit(text, textRect)
        pygame.display.update([rect, textRect])
    
        