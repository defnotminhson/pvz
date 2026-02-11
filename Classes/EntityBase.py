import pygame
from Utils.Game.AnimationHandler import Animator

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2, size: pygame.Vector2):
        super().__init__()

        self.size = size
        self.position = pygame.Vector2(position)

        # Default blank surfac
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

        # Core systems
        self.Animator = Animator()

        # Stats
        self.hp = 100
        self.alive = True

    def update(self):
        if not self.alive:
            return

        self.Animator.update()

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        self.alive = False
        self.kill()
