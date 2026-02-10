import pygame

class AnimationTrack: 
    def __init__(self, sprite: pygame.sprite.Sprite):
        self.frames = []
        self.currentFrame = 0
        self.frameCount = 0
        self.sprite = sprite

    def loadAnimation(self, folder, frameCount):
        self.frames = []
        self.frameCount = frameCount
        for i in range(0,frameCount):
            self.frames.append(pygame.image.load(f"{folder}/frame{frameCount:04d}"))
        return self.frames
    
class Animator:
    def __init__(self, dt: float, fps: int):
        self.dt = dt
        self.fps = fps

    def playAnimation(self, animationTrack: AnimationTrack):
        sprite = animationTrack.sprite 
        frames = animationTrack.frames

        currentFrame = animationTrack.currentFrame
        if currentFrame == self.frameCount:
            animationTrack.currentFrame = 0
            currentFrame = 0

        sprite.image = frames[currentFrame]
        animationTrack.currentFrame += 1
        
        

