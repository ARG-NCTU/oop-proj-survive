import pygame
import Robot

class Enemy(Robot.Robot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((0, 0, 255))
        self.speed = 2
    def update(self):
        pass
    def draw(self, screen):
        super().draw(screen)
