import pygame
import Setting as s

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = direction

        self.lifetime = 5*60 #how many loops the bullet will last for

    def update(self):
        #move the bullet in the direction it was shot
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y
        if self.lifetime > 0:
            self.lifetime -= 1
        else:
            self.kill()

    def draw(self, screen):
        x, y = self.rect.x, self.rect.y
        screen.blit(self.image, (x, y))

    def covert_xy_to_pygame(self, x, y):
        return x, s.HEIGHT - y
    
    def convert_xy_to_pymunk(self, x, y):
        return x, s.HEIGHT - y
