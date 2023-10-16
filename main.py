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
    
    # font = pygame.font.Font(basicFontConfig.name, basicFontConfig.size)
    # rect = pygame.Rect(100, 100, 100, 25)
    # buttonSurface = pygame.Surface((200, 200))
    # text = font.render("buttonText", True, basicFontConfig.textColor, basicFontConfig.buttonColor)
    # textRect = text.get_rect()
    # textRect.center = (100, 100)
    # buttonSurface.blit(text, textRect)
    # pygame.display.update(textRect)
    
    b: B.Button = B.Button(200, 200, basicFontConfig)
    b.draw(screen)

    # b1: B.Button = B.Button(0, 0, basicFontConfig, buttonText="some realllllly long button")
    # b1.draw(screen)
    
    t: T.Text = T.Text(100, 100, "Hello World", basicFontConfig)
    t.draw(screen)
    
    pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)

    
    # pygame.display.update(pygame.draw.circle(screen, RED, PLAYER_POSITION, 10))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        b.process(screen)
    
        
    
    
    
    
    # pygame.init()
    # screen: pygame.surface.Surface = pygame.display.set_mode((640, 480))
    # small_screen: pygame.surface.Surface = pygame.surface.Surface((640/2, 480/2))
    # rect: pygame.rect
    # buttonRect = pygame.Rect(0, 0, 100, 100)
    # small_screen.blit(buttonRect)
    # small_screen.fill(RED)
    # screen.fill(WHITE)
    # screen.blit(small_screen, (0, 0))
    # pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)
    
    # basicFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", WHITE, 10)
    
    # b: B.Button = B.Button(30, 30, basicFontConfig)
    # b.draw(screen)
    
    # b1: B.Button = B.Button(0, 0, basicFontConfig, buttonText="some realllllly long button")
    # b1.draw(screen)
    
    # pygame.display.update()
    
    # screen.fill(BLACK)
    # small_screen.fill(BLUE)
    # pygame.display.update(buttonRect)
    
    # pygame.display.set_caption("Regex Game")
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == RIGHT_KEY:
    #                 PLAYER_POSITION[0] = PLAYER_POSITION[0] + 10
    #             if event.key == LEFT_KEY:
    #                 PLAYER_POSITION[0] = PLAYER_POSITION[0] - 10                
    #             if event.key == BACKWARD_KEY:
    #                 PLAYER_POSITION[1] = PLAYER_POSITION[1] + 10                
    #             if event.key == FORWARD_KEY:
    #                 PLAYER_POSITION[1] = PLAYER_POSITION[1] - 10
    #             screen.fill(WHITE)    
    #             pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)
    #             pygame.display.update()
    #     b.process()
        




if __name__ == "__main__":
    main()
