import pygame,Global
from Classes.Menu.Pointer import Pointer
    
class UiService:
    def __init__(self, screen):
        self.crosshair = Pointer("Assets/Menu/Pointers/Pointer.png")
        self.screen = screen
        self.uiGroup = pygame.sprite.Group()
        self.cards = pygame.sprite.Group()

        self.font = pygame.font.SysFont("comicsansms", 18)
        self.inGameUiHandler = None
        
        self.uiGroup.add(self.crosshair)
    
    def inGameUi(self):
        from Classes.Menu.InGameUi import inGameUi
        self.inGameUiHandler = inGameUi()
    
    def update(self):
        self.cards.draw(self.screen)
        self.cards.update()
        self.uiGroup.draw(self.screen)
        self.uiGroup.update()

        if self.inGameUiHandler:
            self.inGameUiHandler.update()

    def handleClick(self, event):
        for card in self.cards:
            card.handleClick(event)
        
    
