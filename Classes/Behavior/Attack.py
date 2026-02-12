import pygame, Global
from Utils.Game.AnimationHandler import AnimationTrack, Animator

class AttackBehavior:
    def __init__(
            self, 
            attackCoolDown: float,
            animator: Animator, 
            attackAnim: AnimationTrack,
            damage: int,
            entity,
            attackSound: str,
        ):
        self.timePassed = attackCoolDown
        self.attackCoolDown = attackCoolDown
        self.attacking = False
        self.target = "nil"
        self.animator = animator
        self.attackAnim = attackAnim
        self.damage = damage
        self.entity = entity
        self.attackSound = attackSound
    
    def update(self):
        if self.target != "nil":
            self.attacking = True
            self.timePassed += Global.dt
            self.entity.moveBehavior.moving = False
            if self.timePassed >= self.attackCoolDown:
                self.animator.playAnimation(self.attackAnim)
                self.timePassed = 0
                Global.soundHandler.play(self.attackSound)

                self.target.takeDamage(self.damage)
                if self.target.hp <= 0:
                    self.attacking = False
                    self.target = "nil"
                    self.entity.moveBehavior.moving = True