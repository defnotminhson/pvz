import pygame
from Classes.Behavior.Shoot import Shoot

class Cat(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.image = pygame.image.load("Assets/Allies/owo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 110))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.screen = screen
        self.shootBehavior = Shoot(self.screen)
        self.shootBehavior.position = position
    def update(self, dt: float):
        self.shootBehavior.detectAndShoot(dt)
        # glow_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # glow_surface.fill((255, 255, 255, 60))
        # self.screen.blit(glow_surface, self.rect.topleft)