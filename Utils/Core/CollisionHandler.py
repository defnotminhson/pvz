import pygame

def bulletCollision(bulletGr, enemyGr, damage):
    hits = pygame.sprite.groupcollide(bulletGr, enemyGr, True, False)
    for _, enemies in hits.items():
        for enemy in enemies:
            enemy.takeDamage(damage)