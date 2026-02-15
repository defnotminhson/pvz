import pygame, Global
from Classes.Menu.Card import Card
from Classes.Menu.SunIcon import SunIcon
#from Services.UiService import UiService

class inGameUi():
    def __init__(self):
        sunIcon = SunIcon(Global.screen, pygame.Vector2(100,100), 1)
        Global.uiService.uiGroup.add(sunIcon)
        startPos = pygame.Vector2(200,100)
        for i in range(0,10):
            newCard = Card(startPos + pygame.Vector2(i * 95, 0), i)
            newCard.updateInfo()
            Global.uiService.cards.add(newCard)
        
        self.font = pygame.font.SysFont("comicsansms", 18)

    def destroy(self):
        pass

    def update(self):
        pass#self.image.blit(self.sunText, self.textRect)
    