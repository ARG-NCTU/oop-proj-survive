import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        #camera offset
        self.offset = pygame.math.Vector2(0, 0)
        self.half_width = self.display_surface.get_width() / 2
        self.half_height = self.display_surface.get_height() / 2

        #ground
        self.ground_surf = pygame.Surface((2000,2000))
        self.ground_surf.fill((255, 255, 255))
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def custom_draw(self, player):

        self.center_target_camera(player)

        #ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)

        #active elements
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery): #sort the sprites based on their y position
           offset_pos = sprite.rect.topleft - self.offset
           #self.display_surface.blit(sprite.image, offset_pos)
           sprite.draw(self.display_surface)

