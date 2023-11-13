import FontConfig as FC
import GameObject as GO
import GameObjects.Button as B
import Global
import pygame 
import math

class Text(GO.GameObject):
    x: int
    y: int
    message: str
    messageList: list[str]
    fontConfig: FC.FontConfig
    
    fontObject: pygame.font.Font
    textSurface: pygame.Surface
    textSurfaces: list[pygame.Surface]
    width: int
    height: int
    
    def __init__(self, x: int, y: int, message: str, fontConfig: FC.FontConfig, width: int = math.inf) -> None:
        self.x = x
        self.y = y
        self.message = message
        self.messageList = message.split(" ")
        self.fontConfig = fontConfig
        
        self.width = width
        self.fontObject = self.fontConfig.makeFontObject()
        self.height = self.fontObject.size(message)[1]
        self.textSurfaces = self.makeTextSurfaces()
    
    def draw(self, screen)-> None:
        updatedRects = []
        count = 0
        for textSurface in self.textSurfaces: 
            updatedRects.append(screen.blit(textSurface, (self.x, self.y + (self.height * count))))
            count += 1
        pygame.display.update(updatedRects)


    def makeTextSurfaces(self) -> list[pygame.Surface]:
        textSurfaces: list[pygame.Surface] = []
        nextText: str = self.getNextText() 
        while nextText != "":
            textSurfaces.append(self.fontObject.render(nextText, True, self.fontConfig.textColor, self.fontConfig.backgroundColors[B.ButtonState.normal.value]))
            nextText = self.getNextText()
        return textSurfaces
            
    # is is not a functional function so should only be called once it messes up self.messageList
    def getNextText(self) -> str:
        nextText: str = ""
        while len(self.messageList) > 0 and self.getLength(nextText + " " + self.messageList[0]) < self.width:
            nextText += " " + self.messageList.pop(0)
        return nextText
        
    def getLength(self, message: str) -> int:
        return self.fontObject.size(message)[0]
