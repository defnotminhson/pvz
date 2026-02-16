import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class SunGain:
    def __init__(
            self, 
            screen, 
            animator: Animator, 
            position: pygame.Vector2,
            gainAnim: AnimationTrack, 
            gainCoolDown: float,
            hitboxSize: int,
            imageSize: int,
            sunGain: int,
            lane: int,
            gainSound: str,
        ):
        super().__init__()
        self.timePassed = gainCoolDown / 2
        self.gainCoolDown = gainCoolDown
        self.position = position
        self.screen = screen
        self.animator = animator
        self.gainAnim = gainAnim
        self.imageSize = imageSize
        self.hitboxSize = hitboxSize
        self.sunGain = sunGain
        self.lane = lane
        self.gainSound = gainSound

    def update(self):
        self.timePassed += Global.dt
        while self.timePassed >= self.gainCoolDown:
            self.timePassed -= self.gainCoolDown

            Global.inGameSun += self.sunGain
            self.animator.playAnimation(self.gainAnim)
            Global.soundHandler.play(self.gainSound)