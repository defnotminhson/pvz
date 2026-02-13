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
            damage: int,
            lane: int,
            shootSound: str,
        ):
        super().__init__()
        self.timePassed = 0
        self.fireCoolDown = fireCoolDown
        self.bulletSpeed = bulletSpeed
        self.bulletsGroup = bulletGroup
        self.position = position
        self.screen = screen
        self.animator = animator
        self.shootAnim = shootAnim
        self.imageSize = imageSize
        self.hitboxSize = hitboxSize
        self.damage = damage
        self.lane = lane
        self.shootSound = shootSound

    def detectAndShoot(self):
        self.bulletsGroup.draw(self.screen)

        self.timePassed += Global.dt
        while self.timePassed >= self.fireCoolDown:
            self.timePassed -= self.fireCoolDown

            if len(Global.mapService.lanes[self.lane]) == 0:
                break
            self.animator.playAnimation(self.shootAnim)
            Global.soundHandler.play(self.shootSound)
            
            bullet = Bullet(
                position=self.position,
                direction=pygame.Vector2(1, 0),   # right
                speed=self.bulletSpeed,
                hitboxSize=self.hitboxSize,
                imageSize=self.imageSize,
                screen=self.screen,
                damage=self.damage,
            )
            self.bulletsGroup.add(bullet)