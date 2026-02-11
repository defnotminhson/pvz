import pygame

def hitbox_collision(sprite1, sprite2):
    return sprite1.hitbox.colliderect(sprite2.hitbox)

def bulletCollision(bulletGr, enemyGr, damage):
    hits = pygame.sprite.groupcollide(bulletGr, enemyGr, True, False, collided=hitbox_collision)
    for _, enemies in hits.items():
        for enemy in enemies:
            enemy.takeDamage(damage)