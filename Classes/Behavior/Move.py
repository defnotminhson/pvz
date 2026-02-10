import pygame, Global

class Move:
    def __init__(self, rect):
        super().__init__()
        self.direction = pygame.Vector2(-1, 0)  # left
        self.speed = 100
        self.pos = pygame.Vector2(rect.topleft)
        self.rect = rect

    def update(self):
        self.pos += self.direction * self.speed * Global.dt
        self.rect.topleft = self.pos