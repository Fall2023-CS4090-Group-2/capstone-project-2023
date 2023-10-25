import pygame

class Entity:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
