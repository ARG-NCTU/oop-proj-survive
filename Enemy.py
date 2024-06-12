import pygame
import Robot

class Enemy(Robot.Robot):
    def __init__(self, x, y, enemytype):
        super().__init__(x, y)
        self.player_x = 400
        self.player_y = 300
        self.enemytype = enemytype
        if self.enemytype == 0:
            self.health = 100
            self.attack = 10
            self.image.fill((255, 0, 0))
            self.speed = 0.3
        elif self.enemytype == 1:
            self.health = 40
            self.attack = 20
            self.image.fill((0, 255, 0))
            self.speed = 0.5
        else:  
            self.health = 150
            self.attack = 25
            self.image.fill((0, 0, 255))
            self.speed = 0.1
    def update_player_position(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
    def update(self):
        super().update()
        if self.player_x != self.rect.x:
            diection_x = (self.player_x - self.rect.x)/abs(self.player_x - self.rect.x)
        else:
            diection_x = 0
        if self.player_y != self.rect.y:
            diection_y = (self.player_y - self.rect.y)/abs(self.player_y - self.rect.y)
        else:
            diection_y = 0
        super().move(diection_x*self.speed, diection_y*self.speed)
        
    def draw(self, screen):
        super().draw(screen)