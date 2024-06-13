import pygame
import Robot2
import random

class Enemy(Robot2.Robot2):
    def __init__(self, x, y, enemytype):
        super().__init__(x, y)
        self.player_x = 400
        self.player_y = 300
        self.enemytype = enemytype
        if self.enemytype == 0:
            self.health = 100
            self.attack = 10
            pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
            self.speed = 20
        elif self.enemytype == 1:
            self.health = 40
            self.attack = 20
            pygame.draw.circle(self.image, (0, 255, 0), (25, 25), 25)
            self.speed = 30
        else:  
            self.health = 150
            self.attack = 25
            pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25)
            self.speed = 10
    def update_player_position(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
    def update(self):
        super().update()
        if self.player_x != self.rect.x:
            direction_x = (self.player_x - self.rect.x)/abs(self.player_x - self.rect.x)
        else:
            direction_x = 0
        if self.player_y != self.rect.y:
            direction_y = (self.player_y - self.rect.y)/abs(self.player_y - self.rect.y)
        else:
            direction_y = 0
        if self.player_x == self.rect.x and self.player_y == self.rect.y:
            direction_x = random.randint(-3, 3)
            direction_y = random.randint(-3, 3)
        super().move(direction_x*self.speed, direction_y*self.speed)

    def Attacked(self, damage, bullet):
        if self.rect.colliderect(bullet.rect):
            self.health -= damage
            bullet.kill()
         
    def draw(self, screen):
        super().draw(screen)