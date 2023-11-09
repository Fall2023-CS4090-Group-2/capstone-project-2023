import pygame

from entity import Entity

MOVE_DISTANCE = 3

class Player(Entity):
    def __init__(self, x, y, image_path) -> None:
        super().__init__(x, y, image_path)

        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.move_up = False
        self.question_mode = False

    def move(self, screen):
        """
        Move Player with respect to a screen
        """
        if self.move_left and self.rect.x > self.image.get_width() * 0.25:
            self.rect.x -= MOVE_DISTANCE
        if (
            self.move_right
            and self.rect.x < screen.get_width() - self.image.get_width() * 1.25
        ):
            self.rect.x += MOVE_DISTANCE
        if (
            self.move_down
            and self.rect.y < screen.get_height() - self.image.get_height() * 1.25
        ):
            self.rect.y += MOVE_DISTANCE
        if self.move_up and self.rect.y > self.image.get_height() * 0.25:
            self.rect.y -= MOVE_DISTANCE

    def handle_input(self, event) -> None:
        """
        Handles when a user uses the keyboard in "normal" mode. WASD, HJKL, and arrow keys are supported
        """
        # Basic directional movements (allows for holding)
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_h]:
                self.move_left = True
            if event.key in [pygame.K_RIGHT, pygame.K_d, pygame.K_l]:
                self.move_right = True
            if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_j]:
                self.move_down = True
            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_k]:
                self.move_up = True
            # Change to question mode
            if event.key == pygame.K_ESCAPE:
                self.question_mode = True
                self.move_left = False
                self.move_right = False
                self.move_down = False
                self.move_up = False

        # Stop moving after key release
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_h]:
                self.move_left = False
            if event.key in [pygame.K_RIGHT, pygame.K_d, pygame.K_l]:
                self.move_right = False
            if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_j]:
                self.move_down = False
            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_k]:
                self.move_up = False
