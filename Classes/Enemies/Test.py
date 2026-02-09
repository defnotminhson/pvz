import pygame
from Classes.Behavior.Move import Move

class Test(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.image = pygame.image.load("Assets/Enemies/cabi.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 110))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.screen = screen
        self.moveBehavior = Move(self.rect)

        self.hp = 100
        self.moveBehavior.speed = 10

    def takeDamage(self, num: float):
        self.hp -= num
        if self.hp <= 0:
            self.kill()

    def update(self, dt: float):
        self.moveBehavior.update(dt)