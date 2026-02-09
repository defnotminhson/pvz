import pygame

class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, pictureLink):
        super().__init__()
        self.image = pygame.image.load(pictureLink)
        self.rect = self.image.get_rect()