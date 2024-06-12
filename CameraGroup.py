import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        #ground
        self.ground_surf = pygame.Surface(self.display_surface.get_size())
        self.ground_surf.fill((255, 255, 255))
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def custom_draw(self):
        #ground
        self.display_surface.blit(self.ground_surf, self.ground_rect)

        #active elements
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery): #sort the sprites based on their y position
           self.display_surface.blit(sprite.image, sprite.rect)

