import pygame, sys, Global

class EventHandler:
    def __init__(self):
        self.events = pygame.event.get()
    
    def gameLoop(self, tiles):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Global.mapService.handleClick(event)
            Global.allyService.handleClick(event, tiles)
            Global.enemyService.handleClick(event, tiles)
            Global.uiService.handleClick(event)