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

angle = 0

image = pygame.surface.Surface((50, 50))
image.fill((255, 150, 0))
image.set_colorkey((0, 0, 0))
rect = image.get_rect()
rect.center = (100, 100)

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
    #rotate a rectangle
    
    
    old_center = rect.center
    angle += 1
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect()
    rect.center = old_center
    screen.blit(new_image, rect)


    pygame.display.flip()  # Update the display
    clock.tick(FPS) # Cap the frame rate
    #space.step(1/FPS) # Step the physics simulation

    

# Quit Pygame
pygame.quit()