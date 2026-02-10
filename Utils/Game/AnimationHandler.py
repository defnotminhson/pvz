import pygame, Global

class AnimationTrack: 
    def __init__(self, sprite: pygame.sprite.Sprite,  folder: str, frameCount: int, fps: int):
        self.priority = 1
        self.playing = False
        self.Looped = False
        self.timePassed = 0
        self.frameDuration = 1 / fps
        self.frames = []
        self.currentFrame = 0
        self.frameCount = 0
        self.sprite = sprite
        self.frameCount = frameCount
        for i in range(0,frameCount):
            self.frames.append(pygame.image.load(f"{folder}/frame{i:04d}.png"))
    
class Animator:
    def __init__(self):
        self.CurrentAnimation = "nil"

    def playAnimation(self, animationTrack: AnimationTrack):
        animationTrack.timePassed += Global.dt

        sprite = animationTrack.sprite
        frames = animationTrack.frames

        while animationTrack.timePassed >= animationTrack.frameDuration:
            animationTrack.timePassed -= animationTrack.frameDuration
        
            animationTrack.currentFrame = (animationTrack.currentFrame + 1) % len(animationTrack.frames) # loops animation back
            sprite.image = frames[animationTrack.currentFrame]


        


        
        

