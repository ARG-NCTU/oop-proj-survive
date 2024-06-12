import pygame
import Robot

class Enemy(Robot.Robot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((0, 0, 255))
        self.speed = 2
        self.player_x = 400
        self.player_y = 300
    def get_player_position(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
    def update(self):
        if self.player_x < self.rect.x:
            self.rect.x -= self.speed
        if self.player_x > self.rect.x:
            self.rect.x += self.speed
        if self.player_y < self.rect.y:
            self.rect.y -= self.speed
        if self.player_y > self.rect.y:
            self.rect.y += self.speed
    def draw(self, screen):
        super().draw(screen)
