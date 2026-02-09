# models/player.py
from models.base import BaseEntity

class Player(BaseEntity):
    def __init__(self, name: str, hp: int):
        super().__init__(name)
        self.hp = hp

    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp <= 0:
            self.destroy()

    def update(self):
        print(f"{self.name} HP: {self.hp}")
