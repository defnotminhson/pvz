import pygame, Global
from Classes.EntityBase import BaseEntity
from Utils.Game.AnimationHandler import AnimationTrack

class SunFlower(BaseEntity):
    def __init__(self, screen, position: pygame.Vector2, lane: int):
        super().__init__(position=position, hitboxSize=pygame.Vector2(100, 100), imageSize=pygame.Vector2(150, 160), lane=lane)
        self.hp = 30
        self.damage = 10

        self.imageOffset = pygame.Vector2(0,-10)
        self.IdleAnim = AnimationTrack(self, "Assets/Allies/SunFlower/Idle", self.imageSize, 8, Global.animationFPS, True, 1)
        self.Animator.playAnimation(self.IdleAnim)

        self.screen = screen
        
    def update(self):
        super().update()