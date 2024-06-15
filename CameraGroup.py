import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.temp_surface = pygame.Surface((2000, 2000))

        #camera offset
        self.offset = pygame.math.Vector2(0, 0)
        self.half_width = self.display_surface.get_width() / 2
        self.half_height = self.display_surface.get_height() / 2

        #ground
        self.ground_surf = pygame.Surface((2000,2000))
        self.ground_surf.fill((243,243,243))
        # load ground svg image tile and bilt it to the ground surface
        tile = pygame.image.load("assets/background.svg")
        # sclae the tile to make it larger
        tile = pygame.transform.scale(tile, (400, 400))
        #set the alpha value of the tile
        tile.set_alpha(50)
        tile_width = tile.get_width()
        tile_height = tile.get_height()
        for x in range(0, 2000, tile_width):
            for y in range(0, 2000, tile_height):
                self.ground_surf.blit(tile, (x, y))
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height

    def draw_ground(self):
        ground_offset = self.ground_rect.topleft - self.offset
        self.temp_surface.blit(self.ground_surf,(0,0))

    def custom_draw(self, player):

        self.center_target_camera(player)

        #ground
        # ground_offset = self.ground_rect.topleft - self.offset
        # self.temp_surface.blit(self.ground_surf,(0,0))

        #active elements
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery): #sort the sprites based on their y position
           offset_pos = sprite.rect.topleft - self.offset
           #self.display_surface.blit(sprite.image, offset_pos)
           sprite.draw(self.temp_surface)
           #sprite.draw(self.display_surface, self.offset)
        self.display_surface.blit(self.temp_surface, -self.offset)
           

