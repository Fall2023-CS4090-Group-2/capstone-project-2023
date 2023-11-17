import pygame # type: ignore
import random
from typing import List

from player import Player
from enemy import Enemy
from bullet import Bullet
from question import Question, load_questions

from GameObjects.Button import Button
from FontConfig import FontConfig
from GameObjects.Text import Text
from Scene import Scene

TICK_RATE = 128
PADDING = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_YELLOW = (227, 207, 87)


def on_play(parameters: list[object]) -> None:
    parameters[0].on_main_menu = False


def on_exit(parameters: list[object]) -> None:
    parameters[0].running = False


class Game:
    def __init__(self, screen_width, screen_height) -> None:
        self.screen: pygame.surface.Surface = pygame.display.set_mode(
            (screen_width, screen_height)
        )
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

        self.make_main_menu()

    def make_main_menu(self) -> None:
        button_config: FontConfig = FontConfig(
            "freesansbold.ttf", BLACK, (WHITE, LIGHT_YELLOW, None), 32
        )
        text_config: FontConfig = FontConfig(
            "freesansbold.ttf", LIGHT_YELLOW, (None, None, None), 42
        )
        title: Text = Text(465, 35, "Space Invaders", text_config)
        play: Button = Button(
            600,
            200,
            fontConfig=button_config,
            buttonText="Play",
            onClickFunction=on_play,
            parameters=[self],
        )
        exit: Button = Button(
            600,
            300,
            fontConfig=button_config,
            buttonText="Exit",
            onClickFunction=on_exit,
            parameters=[self],
        )

        self.scene: Scene = Scene([title, play, exit], BLACK)

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
            if self.on_main_menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.scene.processMouseClick()

                if event.type == pygame.KEYDOWN:
                    self.scene.processAnyKeyPress(self.screen, event.key)
                    self.scene.draw(self.screen)

        if self.on_main_menu:
            self.scene.processMouseMovement(self.screen)
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
            enemy.move()

        # Update bullet positions
        for bullet in self.bullets:
            # TODO: Removing bullets when off the board
            # if bullet.rect.collidepoint(self.screen.get_width(), self.screen.get_height()):
            #     self.bullets.remove(bullet)
            # else:
            if bullet.rect.x == 750: # Should make this more dynamic
                self.bullets.remove(bullet)
            bullet.move()

        self.handle_collisions()

    def draw(self) -> None:
        """
        Draw all entities on the screen
        """
        if self.on_main_menu:
            self.scene.draw(self.screen)
            return

        if not self.paused:
            # Redraw background
            self.screen.blit(self.background, (0, 0))

            # Update menu
            self.draw_health()
            self.draw_score()
            self.draw_answer()
            self.draw_bullets()

            # Draw question
            self.draw_questions()

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
            self.draw_pause_screen()

        # Tell pygame update its screens
        pygame.display.update()

    def handle_collisions(self) -> None:
        # Handle bullet hitting enemy
        for enemy in self.enemies:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.enemies.remove(enemy) # Can cause a value error
                    self.bullets.remove(bullet)
                    self.score += 1

        # Enemy hitting player
        for enemy in self.enemies:
            if enemy.rect.x < self.player.rect.x + 25:
                self.enemies.remove(enemy)
                self.health -= 5
            if self.health <= 0:
                self.running = False

    def draw_pause_screen(self) -> None:
        """
        Draws pause screen
        """
        self.screen.blit(self.background, (0, 0))
        pygame.draw.rect(self.screen, "white", [380, 150, 510, 50], 0, 10)
        self.screen.blit(
            self.font.render("Game Paused: Press Escape to Resume", True, "black"),
            (400, 160),
        )

    def draw_score(self) -> None:
        """
        Draws score value
        """
        score_str = self.font.render(f"Score: {str(self.score)}", True, (255, 255, 255))
        self.screen.blit(
            score_str,
            (
                score_str.get_width() * 1.75 + PADDING,
                self.font.get_height() - PADDING,
            ),
        )

    def draw_bullets(self) -> None:
        """
        Draws bullet value
        """
        bullet_str = self.font.render(f"Bullet: {str(self.num_bullets)}", True, (255, 255, 255))
        self.screen.blit(
            bullet_str,
            (
                bullet_str.get_width() * 3 + PADDING, # Kind of scuffed position but its there
                self.font.get_height() - PADDING,
            ),
        )

    def draw_health(self) -> None:
        """
        Draws health value
        """
        health_str = self.font.render(
            f"Health: {str(self.health)}", True, (255, 255, 255)
        )
        self.screen.blit(
            health_str,
            (
                PADDING,
                self.font.get_height() - PADDING,
            ),
        )

    def draw_answer(self) -> None:
        """
        Draws your current typed out answer
        """
        if self.player.answer_mode:
            color = LIGHT_YELLOW
        else:
            color = WHITE
        answer_str = self.font.render("Answer: ", True, color)
        self.screen.blit(
            answer_str,
            (
                self.screen.get_width() / 4,
                self.screen.get_height() - self.font.get_height() - PADDING,
            ),
        )
        self.screen.blit(
            self.font.render(self.answer, True, WHITE),
            (
                self.screen.get_width() / 4 + answer_str.get_width(),
                self.screen.get_height() - self.font.get_height() - PADDING,
            ),
        )

    def draw_questions(self) -> None:
        """
        Draws current questions
        """
        height = 50
        # TODO: Align questions to right
        max_width = 0
        for idx, question in enumerate(self.questions):
            if question is self.selected_question:
                color = LIGHT_YELLOW
            else:
                color = WHITE
            question_str = self.font.render(
                f"Question {idx+1}: {question.question}", True, color
            )
            max_width = max(max_width, question_str.get_width())
            self.screen.blit(
                question_str, (self.screen.get_width() - max_width - PADDING, height)
            )
            for option in question.options:
                height += self.font.get_height()
                option_str = self.font.render(option, True, color)
                self.screen.blit(
                    option_str, (self.screen.get_width() - max_width - PADDING, height)
                )
            height += self.font.get_height() * 2

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
                        650, # Should be changed to be dynamic
                        random.randint(0, self.screen.get_height() - 200),
                        "enemy.png",
                    )
                )
