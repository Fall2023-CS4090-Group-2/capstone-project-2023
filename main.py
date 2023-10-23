import pygame, sys
import GameObjects.Button as B
import FontConfig as FC
import GameObjects.Text as T
import GameObject as GO
import Scene as S
import GameObjects.InputField as IF
import Global

WHITE: tuple[int] = (255, 255, 255)
RED: tuple[int]  = (255, 0, 0)
BLUE: tuple[int]  = (0, 0, 255)
BLACK: tuple[int]  = (0, 0, 0)

FORWARD_KEY: int = pygame.K_w
BACKWARD_KEY: int = pygame.K_s
LEFT_KEY: int = pygame.K_a
RIGHT_KEY: int = pygame.K_d

PLAYER_POSITION: list[int] = [100, 100] 

CURRENT_SCENE: S.Scene


def hello() -> None:
    print("hello")
    
def changeScene(scene: list[object]) -> None:
    CURRENT_SCENE = scene[0]
    print(CURRENT_SCENE.buttons)
    CURRENT_SCENE.draw(scene[1])
    pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Regex Game")
    Global.GAME_SCREEN = pygame.display.set_mode((640, 480))
    Global.GAME_SCREEN.fill(WHITE)
    pygame.display.update()
    
    basicFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", BLACK, (RED, BLUE, WHITE), 30)
    basicTextFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", BLACK, (WHITE, BLUE, WHITE), 30)
    
    # sceneTwoText: T.Text = T.Text(100, 100, "This is scene two", basicTextFontConfig)
    # sceneTwo: S.Scene = S.Scene([], [sceneTwoText])
    
    b: B.Button = B.Button(100, 100, basicFontConfig, onClickFunction=hello)
    b1: B.Button = B.Button(200, 200, basicFontConfig, buttonText="some realllllly long button")
    
    t: T.Text = T.Text(100, 0, "Hello World", basicTextFontConfig)

    i: IF.InputField = IF.InputField(300, 300, basicFontConfig, "Hello World")
    
    gameObjects: GO.GameObject = [t, b, b1, i]
    scene: S.Scene = S.Scene(gameObjects)
    scene.draw()
    

    CURRENT_SCENE = scene
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                CURRENT_SCENE.processMouseClick()
            elif event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                CURRENT_SCENE.processAnyKeyPress(event.key)
        CURRENT_SCENE.processMouseMovement()

if __name__ == "__main__":
    main()
