import pygame
from Classes.Menu.Pointer import Pointer
    
class UiService:
    def __init__(self, screen):
        self.crosshair = Pointer("Assets/Menu/Pointers/Pointer.png")
        self.screen = screen
        self.uiGroup = pygame.sprite.Group()
        self.uiGroup.add(self.crosshair)
    
    def update(self):
        self.uiGroup.draw(self.screen)
        self.uiGroup.update()
    
