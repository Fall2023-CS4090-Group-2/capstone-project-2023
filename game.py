import pygame  # type: ignore
import random
from typing import List
from enum import Enum

from player import Player
from enemy import Enemy
from bullet import Bullet
from question import Question, load_questions

from menu import draw_main_menu, draw_pause_menu
from ui import draw_answer, draw_bullets, draw_health, draw_score, draw_questions


from GameObjects.Button import Button
from FontConfig import FontConfig
from GameObjects.Text import Text

# from Scene import Scene

TICK_RATE = 128
PADDING = 10

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_YELLOW = (227, 207, 87)


class State(Enum):
    MAIN_MENU = 0
    RUNNING = 1
    PAUSED = 2

class Game:
    def __init__(self, screen_width, screen_height) -> None:
        self.screen: pygame.surface.Surface = pygame.display.set_mode(
            (screen_width, screen_height)
        )
        self.state: State = State.RUNNING
        self.background = pygame.image.load("background.jpg")
        self.player: Player = Player(PADDING, screen_height / 2, "player.png")
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.num_bullets: int = 50
        self.questions: List[Question] = load_questions()
        self.selected_question: Question = self.questions[0]
        self.answer: str = ""
        self.running: bool = True
        self.paused: bool = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.score = 0
        self.health = 100
        self.on_main_menu = True

    def handle_inputs(self) -> None:
        """
        Handles when a user uses the keyboard. WASD, HJKL, and arrow keys are supported
        """
        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Player movement input
            if not self.player.answer_mode:
                self.player.handle_input(event, self)
            else:
                self.answer_question(event)

            # Bullet movement input
            if event.type == pygame.KEYDOWN and not self.player.answer_mode:
                if event.key == pygame.K_SPACE and self.num_bullets > 0:
                    self.bullets.append(
                        Bullet(
                            self.player.rect.x + PADDING,
                            self.player.rect.y
                            + PADDING
                            - self.player.image.get_height() / 2,
                        )
                    )
                    self.num_bullets -= 1
        self.player.move(self.screen)

    def update(self) -> None:
        """
        Update position of all entities
        """
        # Run no more than TICK_RATE frames per second
        self.clock.tick(TICK_RATE)

        # Add some enemies
        # self.spawn_enemies()

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move(self.screen)

        # Update bullet positions
        for bullet in self.bullets:
            # TODO: Removing bullets when off the board
            # if bullet.rect.collidepoint(self.screen.get_width(), self.screen.get_height()):
            #     self.bullets.remove(bullet)
            # else:
            if bullet.rect.x == 750:  # Should make this more dynamic
                self.bullets.remove(bullet)
            bullet.move()

        self.handle_collisions()

    def draw(self) -> None:
        """
        Draw all entities on the screen
        """

        if not self.paused:
            # Redraw background
            self.screen.blit(self.background, (0, 0))

            # Update menu
            draw_health(self)
            draw_score(self)
            draw_bullets(self)
            draw_answer(self)

            # Draw question
            draw_questions(self)

            # Draw player
            self.player.draw(self.screen)

            # Draw enemy
            for enemy in self.enemies:
                enemy.draw(self.screen)

            # Draw bullet
            for bullet in self.bullets:
                bullet.draw(self.screen)
        else:
            # Draw paused menu if paused
            draw_pause_menu(self)

        draw_main_menu(self)
        # Tell pygame update its screens
        pygame.display.update()

    def handle_collisions(self) -> None:
        # Handle bullet hitting enemy
        for enemy in self.enemies:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.enemies.remove(enemy)  # Can cause a value error
                    self.bullets.remove(bullet)
                    self.score += 1

        # Enemy hitting player
        for enemy in self.enemies:
            if enemy.rect.x < self.player.rect.x + 25:
                self.enemies.remove(enemy)
                self.health -= 5
            if self.health <= 0:
                self.running = False

    def answer_question(self, event) -> None:
        """
        Handles answering a question
        """
        if event.type == pygame.KEYDOWN:
            # Pause screen
            if event.key == pygame.K_ESCAPE:
                self.paused = not self.paused
                return
            # Don't allow answering if paused
            if not self.paused:
                if event.key == pygame.K_RETURN:
                    if self.selected_question.is_correct(self.answer):
                        self.questions.remove(self.selected_question)
                        if len(self.questions) > 0:
                            self.selected_question = self.questions[0]
                    self.answer = ""
                    self.num_bullets += 1
                    self.player.answer_mode = False
                elif event.key == pygame.K_BACKSPACE:
                    self.answer = self.answer[:-1]
                else:
                    self.answer += event.unicode

    def spawn_enemies(self) -> None:
        """
        Spawn enemies
        """
        # TODO: Find a better way of spawn enemies
        if len(self.enemies) == 0:
            for _ in range(6):
                self.enemies.append(
                    Enemy(
                        self.screen.get_width()
                        - 100,  # Should be changed to be dynamic
                        random.randint(0, self.screen.get_height() - 200),
                        "enemy.png",
                    )
                )
