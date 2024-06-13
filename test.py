import pygame
import pymunk

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")
clock = pygame.time.Clock()
FPS = 60

space = pymunk.Space()
LEFT = 50
RIGHT = 950
TOP = 25
BOTTOM = 575
MIDDLEX = (LEFT + RIGHT) / 2
MIDDLEY = (TOP + BOTTOM) / 2

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        #pygame
        super().__init__()
        #craete a circle
        self.image = pygame.Surface((16, 16))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (MIDDLEX, MIDDLEY)
        

        #pymunk
        self.body = pymunk.Body()
        self.body.position = MIDDLEX, MIDDLEY
        self.body.velocity = 400, -300
        self.shape = pymunk.Circle(self.body, 8)
        self.shape.density = 1
        self.shape.elasticity = 1
        #space.add(self.body, self.shape)
        self.shape.collision_type = 1
    
    def draw(self):
        x, y = self.body.position
        screen.blit(self.image, (x - 8, y - 8))
        #pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 8)

class Wall():
    def __init__(self, p1, p2, collision_number=None):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, p1, p2, 10)
        self.shape.elasticity = 1
        space.add(self.body, self.shape)
        if collision_number:
            self.shape.collision_type = collision_number

    def draw(self):
        pygame.draw.line(screen, (255, 255, 255), self.shape.a, self.shape.b, 10)

# Game loop
ball = Ball()
space.add(ball.body, ball.shape)
wall_left = Wall([LEFT, TOP], [LEFT, BOTTOM],2)
wall_right = Wall((RIGHT, TOP), (RIGHT, BOTTOM),2)
wall_top = Wall((LEFT, TOP), (RIGHT, TOP),2)
wall_bottom = Wall((LEFT, BOTTOM), (RIGHT, BOTTOM),2)

running = True
while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    #pygame.display.update()
   
    # Render graphics
    
    screen.fill((0, 0, 0))  # Fill the screen with black
    ball.draw()
    wall_left.draw()
    wall_right.draw()
    wall_top.draw()
    wall_bottom.draw()

    pygame.display.flip()  # Update the display
    clock.tick(FPS) # Cap the frame rate
    space.step(1/FPS) # Step the physics simulation

    

# Quit Pygame
pygame.quit()