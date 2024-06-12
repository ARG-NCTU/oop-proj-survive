import pygame
import Robot

class Enemy(Robot.Robot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((0, 0, 255))
        self.speed = 0.1
        self.player_x = 400
        self.player_y = 300
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