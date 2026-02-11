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

mapService = MapService(screen)
uiService = UiService(screen)
allyService = AllyService(screen)
enemyService = EnemyService(screen)

mapService.mapPos = (325, 100)
mapService.tileSize = (100, 110)

tiles = mapService.createGrid(9, 5, 4, (0, 200, 0, 0)) 

background = pygame.image.load("Assets/Backgrounds/Frontyard.png").convert()
background = pygame.transform.scale(background, (Global.screenWidth + 500, Global.screenHeight))

pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        mapService.handleClick(event)
        allyService.handleClick(event, tiles)
        enemyService.handleClick(event, tiles)

    screen.fill("white")
    screen.blit(background, (0, 0))
    bulletCollision(allyService.bulletGroup, enemyService.enemyGroup, 10)
    enemyCollision(allyService.allyGroup, enemyService.enemyGroup)

    allyService.update()
    enemyService.update()
    mapService.update()
    uiService.update()
    

    pygame.display.flip()
    Global.dt = clock.tick(60) / 1000