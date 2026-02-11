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
            bulletImage: str, 
            bulletSize: pygame.Vector2, 
            bulletSpeed: int
        ):
        super().__init__()
        self.timePassed = 0
        self.fireCoolDown = fireCoolDown
        self.bulletSpeed = bulletSpeed
        self.bulletSize = bulletSize
        self.bulletImage = bulletImage
        self.bulletsGroup = bulletGroup
        self.position = position
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