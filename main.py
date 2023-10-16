import pygame, sys
import Button as B
import FontConfig as FC
import Text as T

WHITE: tuple[int] = (255, 255, 255)
RED: tuple[int]  = (255, 0, 0)
BLUE: tuple[int]  = (0, 0, 255)
BLACK: tuple[int]  = (0, 0, 0)

FORWARD_KEY: int = pygame.K_w
BACKWARD_KEY: int = pygame.K_s
LEFT_KEY: int = pygame.K_a
RIGHT_KEY: int = pygame.K_d

PLAYER_POSITION: list[int] = [100, 100] 

def hello():
    print("hello")

def main():
    pygame.init()
    pygame.display.set_caption("Regex Game")
    screen: pygame.surface.Surface = pygame.display.set_mode((640, 480))
    screen.fill(WHITE)
    pygame.display.update()
    
    basicFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", BLACK, (RED, BLUE, WHITE), 30)
    
    b: B.Button = B.Button(200, 200, basicFontConfig)
    b.draw(screen)

    b1: B.Button = B.Button(0, 0, basicFontConfig, buttonText="some realllllly long button")
    b1.draw(screen)
    
    t: T.Text = T.Text(100, 100, "Hello World", basicFontConfig)
    t.draw(screen)
    
    pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        b.process(screen)
        b1.process(screen)

if __name__ == "__main__":
    main()
