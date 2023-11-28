import pygame  # type: ignore
from pygame.math import Vector2
import random

from entity import Entity
from ui import PADDING
from state import State

MOVE_DISTANCE = 3


class Player(Entity):
    def __init__(self, x, y, image_path) -> None:
        super().__init__(x, y, image_path)

        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.move_up = False
        self.answer_mode = False
        self.enemies_killed = 0
        self.direction = Vector2(1, 0)  # Face right

    def move(self, screen):
        """
        Move Player with respect to a screen
        """
        if self.move_left and self.rect.x > PADDING:
            self.rect.x -= MOVE_DISTANCE
        if (
            self.move_right
            and self.rect.x < screen.get_width() - self.image.get_width()
        ):
            self.rect.x += MOVE_DISTANCE

        if (
            self.move_down
            and self.rect.y < screen.get_height() - self.image.get_height() * 1.25
        ):
            self.rect.y += MOVE_DISTANCE
        if self.move_up and self.rect.y > self.image.get_height() * 0.25:
            self.rect.y -= MOVE_DISTANCE

        # Calculate the direction based on the keys pressed
        direction_x = int(self.move_right) - int(self.move_left)
        direction_y = int(self.move_down) - int(self.move_up)

        # Update the direction vector
        self.direction = Vector2(direction_x, direction_y)

        # Check if the direction vector has non-zero length before normalizing
        if self.direction.length() != 0:
            self.direction.normalize()

    def handle_input(self, event, game) -> None:
        """
        Handles when a user uses the keyboard in "normal" mode. WASD, HJKL, and arrow keys are supported
        """
        # Basic directional movements (allows for holding)
        if event.type == pygame.KEYDOWN:
            # Pause screen
            if event.key == pygame.K_ESCAPE:
                game.state = State.PAUSED
                self.move_left = False
                self.move_right = False
                self.move_down = False
                self.move_up = False
            # Move if not paused
            if game.state == State.RUNNING:
                if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_h]:
                    self.move_left = True
                if event.key in [pygame.K_RIGHT, pygame.K_d, pygame.K_l]:
                    self.move_right = True
                if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_j]:
                    self.move_down = True
                if event.key in [pygame.K_UP, pygame.K_w, pygame.K_k]:
                    self.move_up = True
                # Select question
                if (
                    event.unicode.isdigit()
                    and event.unicode.isdigit()
                    and int(event.unicode) < len(game.selected_question.options) + 1
                    and int(event.unicode) != 0
                ):
                    if game.selected_question.is_correct(
                        game.selected_question.options[int(event.unicode) - 1]
                    ):
                        pygame.mixer.Sound.play(game.correct_sound)
                        game.questions.remove(game.selected_question)
                        game.num_bullets += 1
                        if len(game.questions) > 0:
                            # TODO: Do something here
                            pass
                    else:
                        pygame.mixer.Sound.play(game.incorrect_sound)
                    game.selected_question = random.choice(game.questions)

                # Change to answer mode
                if (
                    event.key == pygame.K_RETURN
                    and len(game.selected_question.options) == 0
                ):
                    self.answer_mode = True
                    self.move_left = False
                    self.move_right = False
                    self.move_down = False
                    self.move_up = False
                if event.key == pygame.K_r:
                    game.selected_question = random.choice(game.questions)

        # Stop moving after key release
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_h]:
                self.move_left = False
            if event.key in [pygame.K_RIGHT, pygame.K_d, pygame.K_l]:
                self.move_right = False
            if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_j]:
                self.move_down = False
            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_k]:
                self.move_up = False
