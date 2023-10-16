import pygame

class FontConfig:
    name: str
    textColor: tuple[int]
    buttonColor: tuple[int]
    size: int
    def __init__(self, name: str, textColor: tuple[int], buttonColor: tuple[int], size: int) -> None:
        self.name = name
        self.textColor = textColor
        self.buttonColor = buttonColor
        self.size = size
        
    def makeFontObject(self) -> pygame.font.Font:
        return pygame.font.Font(self.name, self.size)
        
        