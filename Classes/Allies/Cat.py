import pygame
from Classes.Behavior.Shoot import Shoot

class Cat(pygame.sprite.Sprite):
    def __init__(self, screen, position, bulletGroup):
        super().__init__()
        self.image = pygame.image.load("Assets/Allies/owo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 110))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.screen = screen
        self.bulletGroup = bulletGroup

        self.shootBehavior = Shoot(self.screen, self.bulletGroup)
        self.shootBehavior.position = position

        self.hp = 100
        
    def update(self, dt: float):
        self.shootBehavior.detectAndShoot(dt)