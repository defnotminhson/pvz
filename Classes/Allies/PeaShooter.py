import pygame, Global
from Classes.Behavior.Shoot import Shoot
from Utils.Game.AnimationHandler import AnimationTrack, Animator
from Classes.Projectiles.Bullet import Bullet

class PeaShooter(pygame.sprite.Sprite):
    def __init__(self, screen, position: pygame.Vector2, bulletGroup):
        super().__init__()
        # self.image = pygame.image.load("Assets/Allies/owo.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, (120, 130))
        self.size = pygame.Vector2(150, 160)
        self.IdleAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Idle", self.size, 5, Global.animationFPS, True, 1)
        self.ShootAnim = AnimationTrack(self, "Assets/Allies/PeaShooter/Shoot", self.size, 7, Global.animationFPS, False, 2)
        self.Animator = Animator()
        self.Animator.playAnimation(self.IdleAnim)

        self.image = pygame.image.load("Assets/Allies/PeaShooter/Idle/frame0000.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.screen = screen
        self.bulletGroup = bulletGroup

        self.shootBehavior = Shoot(
            screen=self.screen, 
            position=position + pygame.Vector2(20,-20),
            animator=self.Animator, 
            shootAnim=self.ShootAnim,
            fireCoolDown=2,
            bulletGroup=self.bulletGroup, 
            bulletImage="Assets/Projectiles/Bullet/frame0000.png",
            bulletSize=pygame.Vector2(70,60),
            bulletSpeed=200,
            )

        self.hp = 100
        
    def update(self):
        self.shootBehavior.detectAndShoot()
        self.Animator.update()