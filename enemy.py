import pygame
import random

from entity import Entity


class Enemy(Entity):
    def move(self, screen) -> None:
        self.rect.x -= 1
        # vertical_move = random.choice([-5, 0, 5])
        # if (
        #     self.rect.y + vertical_move
        #     < screen.get_height() - self.image.get_height() * 1.25
        #     and self.rect.y + vertical_move > self.image.get_height() * 0.25
        # ):
        #     self.rect.y += vertical_move
