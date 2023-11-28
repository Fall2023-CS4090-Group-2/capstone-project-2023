from entity import Entity
from difficulty import enemy_stats

import random


class Enemy(Entity):
    def __init__(self, x, y, image_path, speed, damage, score, direction=-1) -> None:
        super().__init__(x, y, image_path)
        self.speed = speed
        self.damage = damage
        self.score = score
        self.direction = direction  # Left = -1, Right = 1

    def move(self) -> None:
        self.rect.x += self.direction * self.speed


def spawn_enemies(game) -> None:
    """
    Spawn enemies
    """
    direction = random.choice([-1, 1])
    for _ in range(enemy_stats[game.difficulty]["max_enemies"]):
        if direction == -1:
            spawn_x = game.screen.get_width() - random.randint(50, 200)
        else:
            spawn_x = -random.randint(50, 200)

        spawn_y = random.randint(50, game.screen.get_height() - 150)

        enemy = Enemy(
            spawn_x,
            spawn_y,
            "boulder.png",
            enemy_stats[game.difficulty]["speed"],
            enemy_stats[game.difficulty]["damage"],
            enemy_stats[game.difficulty]["score"],
            direction,
        )
        game.enemies.append(enemy)
