import pygame  # type: ignore
from entity import Entity

class Bullet(Entity):
    def __init__(self, x, y, direction):
        super().__init__(x, y, "img/pickaxe.png")
        self.speed = 5
        self.rotation_timer = 0
        self.direction = direction

    def move(self):
        """
        Moves bullet
        """
        # Update the bullet's position
        if self.direction.length() != 0:
            movement = self.direction * self.speed
            self.rect.x += int(movement.x)
            self.rect.y += int(movement.y)
        else:
            self.rect.x += self.speed
