import pygame  # type: ignore
from game import Game, State

# Start pygame
pygame.init()
pygame.mixer.init()

# Game window demensions 
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080

# Create game object
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# Game loop
while game.state != State.EXIT:
    game.handle_inputs()
    if game.state == State.RUNNING:
        game.update()
    game.draw()

pygame.quit()
