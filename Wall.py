import pygame
import pymunk
import Setting as s

class Wall(pygame.sprite.Sprite):
    def __init__(self, p1, p2, collision_number=None):
        super().__init__()
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 10)
        self.shape.elasticity = 1
        if collision_number:
            self.shape.collision_type = collision_number

    def draw(self, screen, none):
        pygame.draw.line(screen, (200,200,200), self.shape.a, self.shape.b, 10)


    def draw_gradient_shadow(self, screen, shadow_color, shadow_width, shadow_direction):
        # Direction vector of the wall
        direction = (self.shape.b.x - self.shape.a.x, self.shape.b.y - self.shape.a.y)
        length = pygame.math.Vector2(direction).length()
        
        # Create a surface for the gradient shadow
        gradient_surface = pygame.Surface((int(length), shadow_width), pygame.SRCALPHA)
        
        # Draw the gradient on the surface
        for i in range(shadow_width):
            alpha = int((1 - i / shadow_width) * shadow_color[3])
            color = (shadow_color[0], shadow_color[1], shadow_color[2], alpha)
            pygame.draw.line(gradient_surface, color, (0, i), (length, i))
        
        # Rotate the gradient surface to match the direction of the wall
        angle = pygame.math.Vector2(direction).angle_to((1, 0))
        rotated_surface = pygame.transform.rotate(gradient_surface, -angle)
        
        # Adjust shadow direction based on the wall orientation
        if shadow_direction in ['top']:
            rotated_surface = pygame.transform.flip(rotated_surface, False, True)
        elif shadow_direction in ['left']:
            rotated_surface = pygame.transform.flip(rotated_surface, True, False)

        # Calculate the position to blit the rotated surface
        mid_point = ((self.shape.a.x + self.shape.b.x) / 2, (self.shape.a.y + self.shape.b.y) / 2)
        pos = (mid_point[0] - rotated_surface.get_width() / 2, mid_point[1] - rotated_surface.get_height() / 2)
        
        # Blit the rotated gradient surface onto the screen
        screen.blit(rotated_surface, pos)

    # def draw(self, screen, shadow_direction):
    #     # Define the shadow color (black with transparency)
    #     shadow_color = (0, 0, 0, 100)
    #     shadow_width = 20
        
    #     # Draw the gradient shadow
    #     self.draw_gradient_shadow(screen, shadow_color, shadow_width, shadow_direction)
    #     # Draw the corner of the wall
    #     self.draw_conner(screen)
