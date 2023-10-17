import Button as B
import Text as T
import pygame

class Scene:
    buttons: list[B.Button]
    texts: list[T.Text]
    
    selectedButton: B.Button # I am making the assumption that the mouse can only be over one button at a time or that the buttons can not overlap
    
    def __init__(self, buttons: list[B.Button], texts: list[T.Text]) -> None:
        self.buttons = buttons
        self.texts = texts
        
    def draw(self, screen: pygame.Surface) -> None:
        for button in self.buttons:
            button.draw(screen)
        for text in self.texts:
            text.draw(screen)
    
    def processMouseMovement(self, screen: pygame.Surface) -> None:
        for button in self.buttons:
            if button.processMouseMovement(screen):
                self.selectedButton = button
            
    def processMouseClick(self) -> None:
        if self.selectedButton is not None:
            if self.selectedButton.parameters is not None:
                self.selectedButton.onClickFunction(self.selectedButton.parameters)
            else:
                self.selectedButton.onClickFunction()
                