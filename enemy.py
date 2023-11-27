from entity import Entity
from difficulty import enemy_stats

import random


class Enemy(Entity):
    def __init__(self, x, y, image_path, speed, damage, score) -> None:
        super().__init__(x, y, image_path)
        self.speed = speed
        self.damage = damage
        self.score = score

    def move(self) -> None:
        self.rect.x -= 1 * self.speed

# TODO: Make enemies come from both directions
def spawn_enemies(game) -> None:
    """
    Spawn enemies
    """
    for _ in range(enemy_stats[game.difficulty]["max_enemies"]):
        spawn_x = game.screen.get_width() - random.randint(50, 200)
        spawn_y = random.randint(50, game.screen.get_height() - 150)

        enemy = Enemy(
            spawn_x,
            spawn_y,
            "boulder.png",
            enemy_stats[game.difficulty]["speed"],
            enemy_stats[game.difficulty]["damage"],
            enemy_stats[game.difficulty]["score"],
        )
        game.enemies.append(enemy)
