import pygame

from Services.MapService import MapService
#from Services.EnemyService import enemyService

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

mapService = MapService(screen)
mapService.setPosition(325, 100)
mapService.setSize(100, 110)
tiles = mapService.createGrid(9, 5, 4, (0, 200, 0, 120)) 

background = pygame.image.load("Assets/Backgrounds/Frontyard.png").convert()
background = pygame.transform.scale(background, (screen_width + 500, screen_height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(background, (0, 0))

    mapService.drawGrid()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()