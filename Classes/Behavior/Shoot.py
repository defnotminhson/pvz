import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction: pygame.Vector2, speed, size, bulletImage, screen):
        super().__init__()
        self.image = pygame.image.load(bulletImage).convert_alpha()
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

        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()


class Shoot:
    def __init__(self, screen, bulletGroup, animator: Animator, shootAnim: AnimationTrack):
        super().__init__()
        self.timePassed = 0
        self.fireCoolDown = 1
        self.bulletSpeed = 1000
        self.bulletSize = (50, 50)
        self.bulletImage = "Assets/Projectiles/potato.png"
        self.bulletsGroup = bulletGroup
        self.position = (100,100)
        self.screen = screen
        self.animator = animator
        self.shootAnim = shootAnim

    def detectAndShoot(self):
        self.bulletsGroup.draw(self.screen)

        self.timePassed += Global.dt
        if self.timePassed >= self.fireCoolDown:
            self.animator.playAnimation(self.shootAnim)

            self.timePassed = 0
            
            bullet = Bullet(
                position = self.position,
                direction = pygame.Vector2(1, 0),   # right
                speed = self.bulletSpeed,
                size = self.bulletSize,
                bulletImage = self.bulletImage,
                screen = self.screen
            )
            self.bulletsGroup.add(bullet)