import pygame, Global
from Classes.Behavior.Shoot import Shoot
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack

class PeaShooter(BaseEntity):
    def __init__(self, screen, position: pygame.Vector2, bulletGroup, lane: int):
        super().__init__(position=position, hitboxSize=pygame.Vector2(100, 100), imageSize=pygame.Vector2(150, 160), lane=lane)
        self.hp = 30
        self.damage = 10

        self.IdleAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Idle", self.imageSize, 5, Global.animationFPS, True, 1)
        self.ShootAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Shoot", self.imageSize, 6, Global.animationFPS, False, 2)
        self.Animator.playAnimation(self.IdleAnim)

        self.screen = screen
        self.bulletGroup = bulletGroup

        self.shootBehavior = Shoot(
            screen=self.screen, 
            position=self.position + pygame.Vector2(20,-30),
            animator=self.Animator, 
            shootAnim=self.ShootAnim,
            fireCoolDown=2,
            bulletGroup=self.bulletGroup, 
            bulletSpeed=200,
            hitboxSize=pygame.Vector2(50,50),
            imageSize=pygame.Vector2(80,70),
            damage=self.damage,
            lane=self.lane
            )
        
    def update(self):
        self.shootBehavior.detectAndShoot()
        super().update()