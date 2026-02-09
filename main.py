import pygame, sys

from Services.MapService import MapService
from Services.UiService import UiService
#from Services.EnemyService import enemyService

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
dt = 0

mapService = MapService(screen)
uiService = UiService(screen)

mapService.mapPosX, mapService.mapPosY = 325, 100
mapService.tileSizeX, mapService.tileSizeY = 100, 110

tiles = mapService.createGrid(9, 5, 4, (0, 200, 0, 0)) 

background = pygame.image.load("Assets/Backgrounds/Frontyard.png").convert()
background = pygame.transform.scale(background, (screen_width + 500, screen_height))

pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        mapService.handleClick(event)

    screen.fill("white")
    screen.blit(background, (0, 0))

    mapService.drawGrid()
    uiService.update()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()