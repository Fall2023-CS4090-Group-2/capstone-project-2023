import pygame

class Button():
    fontObject: pygame.font.Font
    x: int
    y: int 
    fontSize: int
    width: int
    height: int
    buttonText: str
    onePress: bool
    
    def __init__(self, x: int, y: int, fontSize: int, buttonText: str = 'Button', width: int = -1, height: int = -1, onclickFunction = None, onePress: bool = False):
        self.fontObject = pygame.font.Font('freesansbold.ttf', fontSize)
        self.x = x
        self.y = y
        self.buttonText = buttonText
        # self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.width = width
        self.height = height
        if self.width == -1:
            self.width = self.fontObject.size(buttonText)[0] + fontSize / 2
        if self.height == -1:
            self.height = self.fontObject.size(buttonText)[1]
            
            
        self.fillColors = {                               
            'normal': '#000000',
            'hover': '#000000',
            'pressed': '#333333',
        }
        
    def draw(self, screen):
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = self.fontObject.render(self.buttonText, True, (20, 20, 20))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
        pygame.display.update(self.buttonRect)
        
        
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
            