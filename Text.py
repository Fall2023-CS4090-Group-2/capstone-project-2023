import FontConfig as FC
import Button as B
import pygame 

class Text:
    x: int
    y: int
    message: str
    fontConfig: FC.FontConfig
    
    fontObject: pygame.font.Font
    textSurface: pygame.Surface
    
    def __init__(self, x: int, y: int, message: str, fontConfig: FC.FontConfig) -> None:
        self.x = x
        self.y = y
        self.message = message
        self.fontConfig = fontConfig
        
        self.fontObject = self.fontConfig.makeFontObject()
        self.textSurface = self.fontObject.render(self.message, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[B.ButtonState.normal.value])
        
    
    def draw(self, screen) -> None:
        updatedRect = screen.blit(self.textSurface, (self.x, self.y))
        pygame.display.update(updatedRect)