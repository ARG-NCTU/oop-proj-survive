import pygame
class Supply(pygame.sprite.Sprite):
    def __init__(self, x, y,supplytype):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image.set_alpha(170)
        self.supplytype = supplytype
        if self.supplytype == 0: #health
            pygame.draw.rect(self.image, (0, 255, 0), (20, 0, 10, 50))
            pygame.draw.rect(self.image, (0, 255, 0), (0, 20, 50, 10))
        elif self.supplytype == 1: #speed
            pygame.draw.polygon(self.image, (100, 0, 0), [(25, 0), (50, 50), (0, 50)])
            pygame.draw.circle(self.image, (255, 255, 0), (25, 33), 15)
        elif self.supplytype == 2: #attack
            pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 25)
            pygame.draw.polygon(self.image, (255, 255, 0), [(25, 0), (30, 20), (50, 20), (35, 30), (40, 50), (25, 35), (10, 50), (15, 30), (0, 20), (20, 20)])
    def update(self):
        pass
    def draw(self, screen, offset):
        x = self.rect.x
        y = self.rect.y
        screen.blit(self.image, (x, y))
        
    
        