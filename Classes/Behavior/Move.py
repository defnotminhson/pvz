import pygame

class Move:
    def __init__(self, rect):
        super().__init__()
        self.direction = (-1, 0)  # left
        self.speed = 30
        self.rect = rect

    def update(self, dt: float):
        self.rect.x += self.direction[0] * self.speed * dt
        self.rect.y += self.direction[1] * self.speed * dt