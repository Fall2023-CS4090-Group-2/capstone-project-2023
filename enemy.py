import pygame

from entity import Entity

class Enemy(Entity):
    def move(self):
        self.rect.y += 1
