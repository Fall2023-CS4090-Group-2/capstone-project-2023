from entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, image_path, speed, damage, score) -> None:
        super().__init__(x, y, image_path)
        self.speed = speed
        self.damage = damage
        self.score = score

    def move(self) -> None:
        self.rect.x -= 1 * self.speed
