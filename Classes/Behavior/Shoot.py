import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, speed, size, bulletImage):
        super().__init__()
        self.image = pygame.image.load(bulletImage).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = direction
        self.speed = speed

    def update(self, dt):
        self.rect.x += self.direction[0] * self.speed * dt
        self.rect.y += self.direction[1] * self.speed * dt


class Shoot:
    def __init__(self, screen):
        super().__init__()
        self.dt = 0
        self.fireCoolDown = 1
        self.bulletSpeed = 300
        self.bulletSize = (50, 50)
        self.bulletImage = "Assets/Projectiles/potato.png"
        self.bulletsGroup = pygame.sprite.Group()
        self.position = (100,100)
        self.screen = screen

    def detectAndShoot(self, dt: float):
        self.bulletsGroup.update(dt)
        self.bulletsGroup.draw(self.screen)

        self.dt += dt
        if self.dt >= self.fireCoolDown:
            self.dt = 0
            
            bullet = Bullet(
                position = self.position,
                direction = (1, 0),   # right
                speed = self.bulletSpeed,
                size = self.bulletSize,
                bulletImage = self.bulletImage
            )
            self.bulletsGroup.add(bullet)