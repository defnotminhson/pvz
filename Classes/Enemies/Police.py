import pygame, Global
from Classes.Behavior.Move import MoveBehavior
from Classes.Behavior.Attack import AttackBehavior
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack

class Police(BaseEntity):
    def __init__(self, screen, position, lane):
        super().__init__(position=position, hitboxSize=pygame.Vector2(40, 100), imageSize=pygame.Vector2(150, 145), lane=lane)
        self.WalkAnim = AnimationTrack(self, "Assets/Enemies/Police/Walk", self.imageSize, 5, Global.animationFPS, True, 1)
        self.AttackAnim = AnimationTrack(self, "Assets/Enemies/Police/Attack", self.imageSize, 10, Global.animationFPS, False, 2)
        self.Animator.playAnimation(self.WalkAnim)
        self.screen = screen
        self.hp = 100
        self.moveBehavior = MoveBehavior(self)
        self.moveBehavior.speed = 15
        self.attackBehavior = AttackBehavior(
            attackCoolDown=1,
            animator=self.Animator,
            attackAnim=self.AttackAnim,
            damage=10,
            entity=self,
            )

    def takeDamage(self, num: float):
        self.hp -= num
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.moveBehavior.update()
        self.attackBehavior.update()
        super().update()