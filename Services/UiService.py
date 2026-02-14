import pygame,Global
from Classes.Menu.Pointer import Pointer
from Classes.Menu.Card import Card
    
class UiService:
    def __init__(self, screen):
        self.crosshair = Pointer("Assets/Menu/Pointers/Pointer.png")
        self.screen = screen
        self.uiGroup = pygame.sprite.Group()
        self.uiGroup.add(self.crosshair)
        self.cards = pygame.sprite.Group()

        startPos = pygame.Vector2(100,100)
        for i in range(0,10):
            newCard = Card(startPos + pygame.Vector2(i * 100, 0), None, None, pygame.Vector2(150,140))
            self.cards.add(newCard)
    
    def update(self):
        self.cards.draw(self.screen)
        self.cards.update()
        self.uiGroup.draw(self.screen)
        self.uiGroup.update()
        
    
