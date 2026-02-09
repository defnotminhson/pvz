import pygame

class Pointer(pygame.sprite.Sprite):
    def __init__(self, pictureLink):
        super().__init__()
        self.image = pygame.image.load(pictureLink)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()