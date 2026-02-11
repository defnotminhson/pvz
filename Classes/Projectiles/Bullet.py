import pygame, Global

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction: pygame.Vector2, speed, size, bulletImage, screen):
        super().__init__()
        self.image = pygame.image.load(bulletImage).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.pos = pygame.Vector2(self.rect.topleft)
        self.direction = direction
        self.speed = speed
        self.screen = screen

    def update(self):
        self.pos += self.direction * self.speed * Global.dt
        self.rect.topleft = self.pos

        if not self.screen.get_rect().colliderect(self.rect):
            self.kill()