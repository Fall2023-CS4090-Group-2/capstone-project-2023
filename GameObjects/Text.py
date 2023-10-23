import FontConfig as FC
import GameObject as GO
import GameObjects.Button as B
import Global
import pygame 

class Text(GO.GameObject):
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
        
    
    def draw(self) -> None:
        updatedRect = Global.GAME_SCREEN.blit(self.textSurface, (self.x, self.y))
        pygame.display.update(updatedRect)