import pygame, pymunk
import Setting as s

class Wall(pygame.sprite.Sprite):
    def __init__(self, p1, p2, collision_number=None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 10)
        self.shape.elasticity = 1
        if collision_number:
            self.shape.collision_type = collision_number

    def draw(self, screen):
        pygame.draw.line(screen, (100, 255, 100), self.shape.a, self.shape.b, 10)