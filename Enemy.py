import pygame
import Robot

class Enemy(Robot.Robot):
    def __init__(self, x, y,player_x, player_y):
        super().__init__(x, y)
        self.image.fill((0, 0, 255))
        self.speed = 2
        self.player_x = player_x
        self.player_y = player_y
    def update_player_position(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
    def update(self):
        robot_x = self.player_x
        robot_y = self.player_y
        if robot_x < self.rect.x:
            self.rect.x -= self.speed
        if robot_x > self.rect.x:
            self.rect.x += self.speed
        if robot_y < self.rect.y:
            self.rect.y -= self.speed
        if robot_y > self.rect.y:
            self.rect.y += self.speed
    def draw(self, screen):
        super().draw(screen)
