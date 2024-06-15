import pygame
class Supply(pygame.sprite.Sprite):
    def __init__(self, x, y,supplytype):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((235, 235, 235))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image.set_alpha(190)
        self.supplytype = supplytype
        pygame.draw.circle(self.image, (255, 255, 185), (25, 25), 25)
        if self.supplytype == 0: #health
            pygame.draw.rect(self.image, (0, 200, 0), (20, 5, 10, 40))
            pygame.draw.rect(self.image, (0, 200, 0), (5, 20, 40, 10))
        elif self.supplytype == 1: #speed
            pygame.draw.polygon(self.image, (100, 0, 0), [(7, 5), (17, 25), (7, 45), (27, 25)])
            pygame.draw.polygon(self.image, (100, 0, 0), [(27, 5), (37, 25), (27, 45), (47, 25)])
        elif self.supplytype == 2: #attack
            #draw a star
            pygame.draw.polygon(self.image, (50, 50, 225), [(25, 5), (30, 20), (45, 20), (35, 30), (40, 45), (25, 35), (10, 45), (15, 30), (5, 20), (20, 20)])
    def update(self):
        pass
    def draw(self, screen):
        x = self.rect.x
        y = self.rect.y
        screen.blit(self.image, (x, y))
        
    
        
        
    
        