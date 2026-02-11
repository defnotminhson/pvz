import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction: pygame.Vector2, speed, bulletImage, size, screen):
        super().__init__()
        self.IdleAnim = AnimationTrack(self, "Assets/Projectiles/Bullet", size, 2, Global.animationFPS, True, 2)
        self.Animator = Animator()
        self.Animator.playAnimation(self.IdleAnim)

        self.image = pygame.image.load("Assets/Projectiles/Bullet/frame0000.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.pos = pygame.Vector2(self.rect.topleft)
        self.direction = direction
        self.speed = speed
        self.screen = screen

    def update(self):
        self.pos += self.direction * self.speed * Global.dt
        self.rect.topleft = self.pos
        self.Animator.update()

        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()