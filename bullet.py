from entity import Entity

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "./bullet.png")

    def move(self):
        self.rect.y -= 5
