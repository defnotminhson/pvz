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

from Utils.Game.SoundHandler import SoundHandler
soundHandler = SoundHandler()
soundHandler.loadFolder("Assets/Sounds")

soundHandler.playMusic("Assets/Sounds/Music/Cerebrawl.mp3")