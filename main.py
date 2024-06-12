import pygame
import Robot

FPS = 60 #frames per second
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 600

#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True

#initialize the robot
all_sprites = pygame.sprite.Group()
Player = Robot.Robot(WIDTH/2, HEIGHT/2)
all_sprites.add(Player)

#game loop 
while running:
    clock.tick(FPS) #FPS frames per second
    #get all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update the game
    all_sprites.update()

    #draw the screen
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()