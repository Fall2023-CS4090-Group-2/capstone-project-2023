import pygame


class Entity:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self) -> None:
        """
        Move entity
        """
        pass

    def draw(self, screen) -> None:
        """
        Draws Entity
        """
        screen.blit(self.image, self.rect)
