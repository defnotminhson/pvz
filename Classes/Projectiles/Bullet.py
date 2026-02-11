import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction: pygame.Vector2, speed, hitboxSize, imageSize, screen):
        super().__init__()
        self.position = position.copy()
        self.IdleAnim = AnimationTrack(self, "Assets/Projectiles/Bullet", imageSize, 2, Global.animationFPS, True, 2)
        self.Animator = Animator()
        self.Animator.playAnimation(self.IdleAnim)

        self.image = pygame.Surface(imageSize, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=self.position)

        self.hitbox = pygame.Rect(0, 0, hitboxSize.x, hitboxSize.y)
        self.hitbox.center = self.position
        
        #self.position = pygame.Vector2(self.rect.topleft)
        self.direction = direction
        self.speed = speed
        self.screen = screen

    def update(self):
        self.position += self.direction * self.speed * Global.dt
        self.rect.topleft = self.position
        self.hitbox.topleft = self.position
        self.Animator.update()

        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()
        
        #pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)