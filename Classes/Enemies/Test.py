import pygame, Global
from Classes.Behavior.Move import Move
from Classes.EntityBase import BaseEntity

class Test(BaseEntity):
    def __init__(self, screen, position):
        super().__init__(position, pygame.Vector2(100, 110))
        self.image = pygame.image.load("Assets/Enemies/cabi.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 110))

        self.screen = screen
        self.moveBehavior = Move(self)

        self.hp = 100
        self.moveBehavior.speed = 10

    def takeDamage(self, num: float):
        self.hp -= num
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.moveBehavior.update()
        super().update()