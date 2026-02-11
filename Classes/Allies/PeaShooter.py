import pygame, Global
from Classes.Behavior.Shoot import Shoot
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class PeaShooter(BaseEntity):
    def __init__(self, screen, position: pygame.Vector2, bulletGroup):
        super().__init__(position, pygame.Vector2(150, 160))
        self.hp = 100

        self.IdleAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Idle", self.size, 5, Global.animationFPS, True, 1)
        self.ShootAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Shoot", self.size, 6, Global.animationFPS, False, 2)
        self.Animator.playAnimation(self.IdleAnim)
        
        self.screen = screen
        self.bulletGroup = bulletGroup

        self.shootBehavior = Shoot(
            screen=self.screen, 
            position=position + pygame.Vector2(20,-30),
            animator=self.Animator, 
            shootAnim=self.ShootAnim,
            fireCoolDown=2,
            bulletGroup=self.bulletGroup, 
            bulletImage="Assets/Projectiles/Bullet/frame0000.png",
            bulletSize=pygame.Vector2(80,70),
            bulletSpeed=200,
            )
        
    def update(self):
        self.shootBehavior.detectAndShoot()
        self.Animator.update()