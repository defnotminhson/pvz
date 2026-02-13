import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame, sys, Global

from Services.MapService import MapService
from Services.UiService import UiService
from Services.AllyService import AllyService
from Services.EnemyService import EnemyService
from Utils.Core.CollisionHandler import bulletCollision, enemyCollision

# pygame setup
pygame.init()
screen = pygame.display.set_mode((Global.screenWidth, Global.screenHeight))
clock = pygame.time.Clock()

Global.mapService = MapService(screen)
Global.uiService = UiService(screen)
Global.allyService = AllyService(screen)
Global.enemyService = EnemyService(screen)

Global.mapService.mapPos = (440, 220)
Global.mapService.tileSize = (80, 75)
tiles = Global.mapService.createGrid(15, 10, 4, (0, 200, 0, 0))

background = pygame.image.load("Assets/Backgrounds/frontyard3.png").convert()
background = pygame.transform.scale(background, (Global.screenWidth + 500, Global.screenHeight + 150))

pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        Global.mapService.handleClick(event)
        Global.allyService.handleClick(event, tiles)
        Global.enemyService.handleClick(event, tiles)

    screen.fill("white")
    screen.blit(background, (0, -100))
    bulletCollision(Global.allyService.bulletGroup, Global.enemyService.enemyGroup)
    enemyCollision(Global.allyService.allyGroup, Global.enemyService.enemyGroup)

    Global.allyService.update()
    Global.enemyService.update()
    Global.mapService.update()
    Global.uiService.update()
    

    pygame.display.flip()
    Global.dt = clock.tick(144) / 1000