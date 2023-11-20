import pygame  # type: ignore
import random
from typing import List

from player import Player
from enemy import Enemy
from bullet import Bullet
from question import Question, load_questions

from difficulty import Difficulty, enemy_stats
from state import State

from menu import draw_main_menu, draw_pause_menu, handle_main_menu, handle_pause_menu
from ui import draw_answer, draw_bullets, draw_health, draw_score, draw_questions

TICK_RATE = 128
PADDING = 10

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_YELLOW = (227, 207, 87)


class Game:
    def __init__(self, screen_width, screen_height) -> None:
        # Game visuals
        self.screen: pygame.surface.Surface = pygame.display.set_mode(
            (screen_width, screen_height)
        )
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.background = pygame.image.load("background.jpg")

        # Game data
        self.state: State = State.RUNNING
        self.difficulty: Difficulty = Difficulty.EASY
        self.answer: str = ""
        self.clock = pygame.time.Clock()
        self.score = 0
        self.health = 100

        # Game entities
        self.player: Player = Player(PADDING, screen_height / 2, "player.png")
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.num_bullets: int = 50
        self.questions: List[Question] = load_questions()
        self.selected_question: Question = self.questions[0]

    def handle_inputs(self) -> None:
        """
        Handle input for all states
        """
        if self.state == State.RUNNING:
            self.handle_running_input()
        elif self.state == State.PAUSED:
            handle_pause_menu(self)
        elif self.state == State.MAIN_MENU:
            handle_main_menu(self)

    def update(self) -> None:
        """
        Update position of all entities
        """
        # Run no more than TICK_RATE frames per second
        self.clock.tick(TICK_RATE)

        # Add some enemies
        self.spawn_enemies()

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move(self.screen)
            # Remove enemy if off screen
            if not self.screen.get_rect().colliderect(enemy.rect):
                self.enemies.remove(enemy)

        # Update bullet positions
        for bullet in self.bullets:
            bullet.move()
            # Remove bullet if off screen
            if not self.screen.get_rect().colliderect(bullet.rect):
                self.bullets.remove(bullet)

        self.handle_collisions()

    def draw(self) -> None:
        """
        Draw all entities on the screen
        """

        if self.state == State.RUNNING:
            self.draw_running()
        elif self.state == State.PAUSED:
            draw_pause_menu(self)
        elif self.state == State.MAIN_MENU:
            draw_main_menu(self)

        # Tell pygame update its screens
        pygame.display.update()

    def handle_running_input(self) -> None:
        """
        Handles when a user plays the game. WASD, HJKL, and arrow keys are supported
        """
        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = State.EXIT

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

    def draw_running(self) -> None:
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

    def handle_collisions(self) -> None:
        # Handle bullet hitting enemy
        for enemy in self.enemies:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.score += enemy.score
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)

        # Enemy hitting player
        for enemy in self.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.enemies.remove(enemy)
                self.health -= enemy.damage
            if self.health <= 0:
                self.state = State.EXIT

    def answer_question(self, event) -> None:
        """
        Handles answering a question
        """
        if event.type == pygame.KEYDOWN:
            # Pause screen
            if event.key == pygame.K_ESCAPE:
                self.state = State.PAUSED
                return
            # Don't allow answering if paused
            if self.state != State.PAUSED:
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
            for _ in range(enemy_stats[self.difficulty]["max_enemies"]):
                spawn_x = self.screen.get_width() - random.randint(50, 200)
                spawn_y = random.randint(50, self.screen.get_height() - 150)

                enemy = Enemy(
                    spawn_x,
                    spawn_y,
                    "enemy.png",
                    enemy_stats[self.difficulty]["speed"],
                    enemy_stats[self.difficulty]["damage"],
                    enemy_stats[self.difficulty]["score"],
                )
                self.enemies.append(enemy)
