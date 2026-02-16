import pygame, Global
from Classes.Menu.Card import Card
from Classes.Menu.SunIcon import SunIcon
from Classes.Menu.Components.TextLabel import TextLabel
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
        
        self.sunLabel = TextLabel(str(Global.inGameSun), (100, 135), 24, (255,255,50), "Assets/Fonts/Rimouski.OTF", True)
        Global.uiService.uiGroup.add(self.sunLabel)
    def destroy(self):
        pass

    def update(self):
        self.sunLabel.setText(str(Global.inGameSun))
    