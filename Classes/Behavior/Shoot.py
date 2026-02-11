import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator
from Classes.Projectiles.Bullet import Bullet


class Shoot:
    def __init__(
            self, 
            screen, 
            animator: Animator, 
            position: pygame.Vector2,
            shootAnim: AnimationTrack, 
            fireCoolDown: float,
            bulletGroup: pygame.sprite.Group, 
            bulletSpeed: int,
            hitboxSize: int,
            imageSize: int,
        ):
        super().__init__()
        self.timePassed = fireCoolDown
        self.fireCoolDown = fireCoolDown
        self.bulletSpeed = bulletSpeed
        self.bulletsGroup = bulletGroup
        self.position = position
        self.screen = screen
        self.animator = animator
        self.shootAnim = shootAnim
        self.imageSize = imageSize
        self.hitboxSize = hitboxSize

    def detectAndShoot(self):
        self.bulletsGroup.draw(self.screen)

        self.timePassed += Global.dt
        while self.timePassed >= self.fireCoolDown:
            self.animator.playAnimation(self.shootAnim)

            self.timePassed -= self.fireCoolDown
            
            bullet = Bullet(
                position = self.position,
                direction = pygame.Vector2(1, 0),   # right
                speed = self.bulletSpeed,
                hitboxSize = self.hitboxSize,
                imageSize = self.imageSize,
                screen = self.screen
            )
            self.bulletsGroup.add(bullet)