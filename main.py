import pygame
from game import Game

# Start pygame
pygame.init()

# Game window demensions 
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

# Create game object
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# Game loop
while game.running:
    game.handle_inputs()
    if not game.paused:
        game.update()
    game.draw()

pygame.quit()
