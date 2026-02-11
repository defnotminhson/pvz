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

        cache_key = (folder, tuple(size), frameCount)

        if cache_key not in Global.animationCache:
            frames = []
            for i in range(frameCount):
                img = pygame.image.load(f"{folder}/frame{i:04d}.png").convert_alpha()
                img = pygame.transform.scale(img, size)
                frames.append(img)

            Global.animationCache[cache_key] = frames

        self.frames = Global.animationCache[cache_key]

        # for i in range(0,frameCount):
        #     self.frames.append(pygame.transform.scale(pygame.image.load(f"{folder}/frame{i:04d}.png"), self.size))
    
class Animator:
    def __init__(self):
        self.CurrentAnimations = {}

    def playAnimation(self, animationTrack: AnimationTrack):
        self.CurrentAnimations[animationTrack.priority] = animationTrack

    def update(self):
        if self.CurrentAnimations == {}:
            return
        
        highest = max(self.CurrentAnimations)
        animationTrack : AnimationTrack = self.CurrentAnimations[highest]
        animationTrack.timePassed += Global.dt

        sprite = animationTrack.sprite
        frames = animationTrack.frames

        while animationTrack.timePassed >= animationTrack.frameDuration:
            if animationTrack.timePassed >= animationTrack.frameDuration * animationTrack.frameCount and not animationTrack.Looped:
                animationTrack.timePassed = 0
                self.CurrentAnimations.pop(highest, None)
                break
            animationTrack.timePassed -= animationTrack.frameDuration
        
            animationTrack.currentFrame += 1
            if animationTrack.currentFrame >= animationTrack.frameCount:
                if animationTrack.Looped:
                    animationTrack.currentFrame = 0
                else:
                    animationTrack.currentFrame = 0
                    self.CurrentAnimations.pop(highest, None)
                    break

            sprite.image = frames[animationTrack.currentFrame]
        


        


        
        

