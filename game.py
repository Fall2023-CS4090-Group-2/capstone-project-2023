import pygame
import random
from typing import List

from player import Player
from enemy import Enemy
from bullet import Bullet

TICK_RATE = 128
# TODO: Remove this and get from self.screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


class Game:
    def __init__(self, screen_width, screen_height) -> None:
        self.screen: pygame.surface.Surface = pygame.display.set_mode(
            (screen_width, screen_height)
        )
        self.player: Player = Player(screen_width / 2, screen_height - 75, "player.png")
        self.enemies: List[Enemy] = []
        self.bullets: List[Bullet] = []
        self.running: bool = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.score = 0
        self.health = 100

    def handle_inputs(self) -> None:
        """
        Handles when a user uses the keyboard. WASD and arrow keys are supported
        """
        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Player movement input
            self.player.handle_input(event)

            # Bullet movement input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append(
                        Bullet(self.player.rect.x - 10, self.player.rect.y - 10)
                    )
                    # TODO: Make it to where you can hold space bar down
        self.player.move()

    def update(self) -> None:
        """
        Update position of all entities
        """
        # Run no more TICK_RATE frames per second
        self.clock.tick(TICK_RATE)

        # Add some enemies
        self.spawn_enemies()

        # Update enemy positions
        for enemy in self.enemies:
            enemy.move()

        # Update bullet positions
        for bullet in self.bullets:
            bullet.move()

        self.handle_collisions()

    def draw(self) -> None:
        """
        Draw all entities on the screen
        """
        # Redraw background
        self.screen.fill((0, 0, 0))

        # Update menu
        self.draw_health()
        self.draw_score()

        # Draw player
        self.player.draw(self.screen)

        # Draw enemy
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Draw bullet
        for bullet in self.bullets:
            bullet.draw(self.screen)

        # Tell pygame update its screens
        pygame.display.update()

    def handle_collisions(self) -> None:
        # Handle bullet hitting enemy
        for enemy in self.enemies:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.score += 1

        # Enemy hitting player
        for enemy in self.enemies:
            if enemy.rect.y > self.player.rect.y - 100:
                self.enemies.remove(enemy)
                self.health -= 5
            if self.health <= 0:
                self.running = False

    def draw_score(self) -> None:
        """
        Draws score value
        """
        score_str = self.font.render(f"Score: {str(self.score)}", True, (255, 255, 255))
        self.screen.blit(score_str, (20, 20))

    def draw_health(self) -> None:
        """
        Draws health value
        """
        health_str = self.font.render(
            f"Health: {str(self.health)}", True, (255, 255, 255)
        )
        self.screen.blit(health_str, (SCREEN_WIDTH - 150, 20))

    def spawn_enemies(self) -> None:
        """
        Spawn enemies
        """
        # TODO: Find a better way of spawn enemies
        if len(self.enemies) == 0:
            for _ in range(6):
                self.enemies.append(
                    Enemy(
                        random.randint(0, SCREEN_WIDTH - 200),
                        random.randint(0, 20),
                        "enemy.png",
                    )
                )
