import pygame
from typing import List
import random
from bullet import Bullet

from enemy import Enemy
from player import Player

SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

# Start pygame
pygame.init()

font = pygame.font.Font("freesansbold.ttf", 24)

def update_score(score: int, screen):
    score_str = font.render(f"Score: {str(score)}", True, (255, 255, 255))
    screen.blit(score_str, (20, 20))

def update_health(health: int, screen):
    health_str = font.render(f"Health: {str(health)}", True, (255, 255, 255))
    screen.blit(health_str, (SCREEN_WIDTH - 150, 20))

screen: pygame.surface.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 75, "player.png")
clock = pygame.time.Clock()
score: int = 0
health: int = 100

bullets: List[Bullet] = []
enemies: List[Enemy] = []

running = True
while running:
    clock.tick(128)

    # Draw background (maybe look into using dirty rectangle)
    screen.fill((0, 0, 0))
    if len(enemies) == 0:
        for _ in range(6):
            enemies.append(Enemy(random.randint(0, SCREEN_WIDTH - 200), random.randint(0, 20), "enemy.png"))

    # Handle keyboard input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement input
        player.handle_input(event)

        # Bullet movement input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.x - 10, player.rect.y - 10))
                # TODO: Make it to where you can hold space bar down 
    player.move()

    # Handle shooting bullets
    for bullet in bullets:
        bullet.move()
        bullet.draw(screen)

    # Handle enemies
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    # Handle bullet hitting enemy
    for enemy in enemies:
        for bullet in bullets:
            if enemy.rect.colliderect(bullet.rect):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1

    # Enemy hitting player
    for enemy in enemies:
        if enemy.rect.y > player.rect.y - 100:
            enemies.remove(enemy)
            health -= 5
        if health <= 0:
            running = False

    # Update
    update_score(score, screen)
    update_health(health, screen)
    player.draw(screen)
    pygame.display.update()
