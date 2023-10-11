import pygame, sys
import Button

WHITE: tuple[int] = (255, 255, 255)
RED: tuple[int]  = (255, 0, 0)

FORWARD_KEY: int = pygame.K_w
BACKWARD_KEY: int = pygame.K_s
LEFT_KEY: int = pygame.K_a
RIGHT_KEY: int = pygame.K_d

PLAYER_POSITION: list[int] = [100, 100] 

def hello():
    print("hello")

def main():
    pygame.init()
    screen: pygame.surface.Surface = pygame.display.set_mode((640, 480))
    screen.fill(RED)
    pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)
    b: Button.Button = Button.Button(30, 30, 10)
    b.draw(screen)
    pygame.display.update()
    pygame.display.set_caption("Regex Game")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == RIGHT_KEY:
                    PLAYER_POSITION[0] = PLAYER_POSITION[0] + 10
                if event.key == LEFT_KEY:
                    PLAYER_POSITION[0] = PLAYER_POSITION[0] - 10                
                if event.key == BACKWARD_KEY:
                    PLAYER_POSITION[1] = PLAYER_POSITION[1] + 10                
                if event.key == FORWARD_KEY:
                    PLAYER_POSITION[1] = PLAYER_POSITION[1] - 10
                screen.fill(WHITE)    
                pygame.draw.circle(screen, RED, PLAYER_POSITION, 10)
                pygame.display.update()
        b.process()
        




if __name__ == "__main__":
    main()
