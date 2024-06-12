import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        #Attributes
        self.speed = 5
        self.health = 100
        self.level = 1

    def update(self):
       pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
