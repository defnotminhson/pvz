import pygame

def to4Digits(n):
    return str(n).zfill(4)

class Animation: 
    def __init__(self):
        self.frames = []
        self.currentFrame = 0

    def loadAnimation(self, folder, frameCount):
        self.frames = []
        for i in range(0,frameCount):
            self.frames.append(pygame.image.load(f"{folder}/frame{frameCount:04d}"))
        return self.frames
    
    def updateAnimation(self, frames, currentFrame, dt):
        self.currentFrame += 1
        self.image = frames[currentFrame]
        

