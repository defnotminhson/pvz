import pygame, Global
from Utils.Game.Highlight import highlight

class Card(pygame.sprite.Sprite):
    def __init__(self, position, price: int, allyName: str, size: pygame.Vector2):
        super().__init__()
        self.size = size
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Menu/Card.png").convert_alpha(), self.size)
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hitbox = pygame.Rect(0, 0, size.x - 50, size.y - 30)
        self.hitbox.center = position
        self.price = price
        self.allyName = allyName

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        # hover glow
        if self.hitbox.collidepoint(mouse_pos):
            highlight(self.size - pygame.Vector2(50,20), self.rect.topleft + pygame.Vector2(25,10), Global.screen, (0,0,0, 60))