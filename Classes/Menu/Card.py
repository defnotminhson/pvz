import pygame, Global

class Card(pygame.sprite.Sprite):
    def __init__(self, position, price: int, allyName: str):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Assets/Menu/Card.png"), pygame.Vector2(100,120))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.price = price
        self.allyName = allyName