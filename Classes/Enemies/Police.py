import pygame, Global
from Classes.Behavior.Move import Move
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack

class Police(BaseEntity):
    def __init__(self, screen, position):
        super().__init__(position=position, hitboxSize=pygame.Vector2(30, 100), imageSize=pygame.Vector2(150, 145))
        self.WalkAnim = AnimationTrack(self, "Assets/Enemies/Police/Walk", self.imageSize, 5, Global.animationFPS, True, 1)
        self.ShootAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Shoot", self.imageSize, 6, Global.animationFPS, False, 2)
        self.Animator.playAnimation(self.WalkAnim)

        self.screen = screen
        self.moveBehavior = Move(self)

        self.hp = 100
        self.moveBehavior.speed = 15

    def takeDamage(self, num: float):
        self.hp -= num
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.moveBehavior.update()
        super().update()