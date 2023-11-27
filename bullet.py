from entity import Entity


class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, "./pickaxe.png")

    def move(self):
        """
        Moves bullet
        """
        # TODO: Update to make the bullet fire in the direction the player is facing
        self.rect.x += 5
