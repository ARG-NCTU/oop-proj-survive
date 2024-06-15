import pygame
import io

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")
clock = pygame.time.Clock()
FPS = 60

# Load the background image 
# turn the svg image to a png image
background = pygame.image.load("assets/background.svg")
#pygame.image.save(backgroun_svg, "assets/background.png")
#background = pygame.image.load("assets/background.png")
#to avoid the black background
#background.set_colorkey((0,0,0))


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render graphics
    screen.fill((100, 100, 150))  # Fill the screen with a background color
    screen.blit(background, (0, 0))  # Blit the background image onto the screen

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Cap the frame rate

# Quit Pygame
pygame.quit()
