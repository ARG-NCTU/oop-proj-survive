import pygame

class Bullet:
    def __init__(self, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  
        self.speed = speed
        self.direction = direction

    def update(self):
        #move the bullet in the direction it was shot
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if self.rect.x < 0 or self.rect.x > 2000 or self.rect.y < 0 or self.rect.y > 2000:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)
