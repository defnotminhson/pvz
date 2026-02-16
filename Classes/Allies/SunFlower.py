import pygame, Global
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack
from Classes.Behavior.SunGain import SunGain

class SunFlower(BaseEntity):
    def __init__(self, screen, position: pygame.Vector2, lane: int):
        super().__init__(position=position, hitboxSize=pygame.Vector2(100, 100), imageSize=pygame.Vector2(150, 160), lane=lane)
        self.hp = 30
        self.damage = 10
        self.sunGain = 25
        self.coolDown = 5

        self.imageOffset = pygame.Vector2(0,-10)
        self.IdleAnim = AnimationTrack(self, "Assets/Allies/SunFlower/Idle", self.imageSize, 2, 6, True, 1)
        self.gainAnim = AnimationTrack(self, "Assets/Allies/SunFlower/Gain", self.imageSize, 8, Global.animationFPS, False, 2)
        self.Animator.playAnimation(self.IdleAnim)

        self.screen = screen
        self.timePassed = 0
        self.sunGainBehavior = SunGain(
            screen=Global.screen,
            animator=self.Animator,
            position=self.position,
            gainAnim=self.gainAnim,
            gainCoolDown=self.coolDown,
            hitboxSize=self.hitboxSize,
            imageSize=self.imageSize,
            sunGain=self.sunGain,
            lane=self.lane,
            gainSound="Effect/sunCollect",
        )
        
    def update(self):
        self.sunGainBehavior.update()
        super().update()