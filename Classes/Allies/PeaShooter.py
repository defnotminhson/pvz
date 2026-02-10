import pygame, Global
from Classes.Behavior.Shoot import Shoot
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class PeaShooter(pygame.sprite.Sprite):
    def __init__(self, screen, position, bulletGroup):
        super().__init__()
        # self.image = pygame.image.load("Assets/Allies/owo.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (120, 130))
        self.IdleAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Idle", 5, Global.animationFPS)
        self.ShootAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Shoot", 7, Global.animationFPS)
        self.Animator = Animator()

        self.image = pygame.image.load("Assets/Allies/PeaShooter/Idle/frame0000.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.screen = screen
        self.bulletGroup = bulletGroup

        self.shootBehavior = Shoot(self.screen, self.bulletGroup)
        self.shootBehavior.position = position

        self.hp = 100
        self.shootBehavior.bulletSpeed = 200
        
    def update(self):
        self.shootBehavior.detectAndShoot()