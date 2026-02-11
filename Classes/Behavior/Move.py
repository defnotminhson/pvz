import pygame, Global

class Move:
    def __init__(self, entity):
        super().__init__()
        self.direction = pygame.Vector2(-1, 0)  # left
        self.speed = 100
        self.entity = entity
        self.moving = True

    def update(self):
        if self.moving:
            self.entity.position += self.direction * self.speed * Global.dt