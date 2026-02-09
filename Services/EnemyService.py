from Services.MapService import mapService

class enemyService:
    def __init__(self, name: str):
        self.name = name
        self.active = True

    def update(self):
        pass

    def destroy(self):
        self.active = False