import pygame
from Utils.Game.AnimationHandler import Animator

class BaseEntity(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2, hitboxSize: pygame.Vector2, imageSize: pygame.Vector2, lane: int):
        super().__init__()

        self.hitboxSize = hitboxSize
        self.imageSize = imageSize
        self.position = position
        self.lane = lane

        self.hitbox = pygame.Rect(0, 0, hitboxSize.x, hitboxSize.y)
        self.hitbox.center = self.position
        # Default blank surface
        self.image = pygame.Surface(imageSize, pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)

        # Core systems
        self.Animator = Animator()

        # Stats
        self.hp = 100
        self.damage = 10
        self.alive = True

    def update(self):
        if not self.alive:
            return

        self.Animator.update()
        self._update_rect()

    def _update_rect(self):
        self.rect.center = self.position
        self.hitbox.center = self.position

    def takeDamage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.die()

    def die(self):
        self.alive = False
        self.kill()
