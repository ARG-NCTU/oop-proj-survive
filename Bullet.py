import pygame
import Setting as s

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.covert_xy_to_pygame(x, y)
        self.speed = speed
        self.direction = direction

    def update(self):
        #move the bullet in the direction it was shot
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y
        #if self.rect.x < 0 or self.rect.x > 2000 or self.rect.y < 0 or self.rect.y > 2000:
           # self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def covert_xy_to_pygame(self, x, y):
        return x, s.HEIGHT - y
