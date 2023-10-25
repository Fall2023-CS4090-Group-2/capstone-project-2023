import pygame

from entity import Entity


class Player(Entity):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

        self.move_left = False
        self.move_right = False

    def move(self):
        if self.move_right and self.rect.x < 1050:
            self.rect.x += 3
        if self.move_left and self.rect.x > 0:
            self.rect.x -= 3

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.move_left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.move_left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.move_right = False
