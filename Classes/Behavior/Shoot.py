import pygame

class Shoot:
    def __init__(self, dt: float, imageLink: str):
        self.dt = dt
        self.size = (50, 50)
        self.image = pygame.image.load(imageLink).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

    def setSize(self, size):
        self.size = size
        self.image = pygame.transform.scale(self.image, self.size)