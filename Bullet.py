import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  
        self.speed = speed
        self.direction = direction

    def update(self):
        #move the bullet in the direction it was shot
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y
        if self.rect.x < 0 or self.rect.x > 2000 or self.rect.y < 0 or self.rect.y > 2000:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
