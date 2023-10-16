import pygame

class FontConfig:
    name: str
    textColor: tuple[int]
    backgroundColors: tuple[int] # should be length three because that is all the states in the ButtonState enum
    size: int
    def __init__(self, name: str, textColor: tuple[int], backgroundColors: tuple[tuple[int]], size: int) -> None:
        self.name = name
        self.textColor = textColor
        self.backgroundColors = backgroundColors
        self.size = size
        
    def makeFontObject(self) -> pygame.font.Font:
        return pygame.font.Font(self.name, self.size)
        
        