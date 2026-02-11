import pygame, Global

class AnimationTrack: 
    def __init__(self, sprite: pygame.sprite.Sprite,  folder: str, size: pygame.Vector2, frameCount: int, fps: int, looped: bool, priority: int):
        self.priority = priority
        self.playing = False
        self.Looped = looped
        self.size = size
        self.timePassed = 0
        self.frameDuration = 1 / fps
        self.frames = []
        self.currentFrame = 0
        self.frameCount = 0
        self.sprite = sprite
        self.frameCount = frameCount
        for i in range(0,frameCount):
            self.frames.append(pygame.transform.scale(pygame.image.load(f"{folder}/frame{i:04d}.png"), self.size))
    
class Animator:
    def __init__(self):
        self.CurrentAnimations = {}

    def playAnimation(self, animationTrack: AnimationTrack):
        self.CurrentAnimations[animationTrack.priority] = animationTrack

    def update(self):
        if self.CurrentAnimations == {}:
            return
        
        for i in sorted(self.CurrentAnimations): # going from the lowest to make the higher priority animation overwrites
            animationTrack : AnimationTrack = self.CurrentAnimations[i]
            animationTrack.timePassed += Global.dt

            sprite = animationTrack.sprite
            frames = animationTrack.frames

            while animationTrack.timePassed >= animationTrack.frameDuration:
                animationTrack.timePassed -= animationTrack.frameDuration
            
                animationTrack.currentFrame += 1
                if animationTrack.currentFrame >= animationTrack.frameCount:
                    if animationTrack.Looped:
                        animationTrack.currentFrame = 0
                    else:
                        animationTrack.currentFrame = 0
                        self.CurrentAnimations.pop(i, None)
                        break
                #print(animationTrack.currentFrame)
                if i == max(self.CurrentAnimations):
                    sprite.image = frames[animationTrack.currentFrame]


        


        
        

