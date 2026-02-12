screenWidth = 1280
screenHeight = 720
dt = 0
animationFPS = 12
animationCache = {}

from Services.MapService import MapService
from Services.UiService import UiService
from Services.AllyService import AllyService
from Services.EnemyService import EnemyService
mapService : MapService = None
uiService : UiService = None
allyService : AllyService = None
enemyService : EnemyService = None