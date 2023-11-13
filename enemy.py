import pygame

from entity import Entity


class Enemy(Entity):
    def move(self) -> None:
        self.rect.y += 1
