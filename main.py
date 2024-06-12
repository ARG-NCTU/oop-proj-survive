import pygame
import Robot, Enemy, CameraGroup

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
player = Robot.Robot(WIDTH/2, HEIGHT/2)
all_sprites.add(player)

enemy = Enemy.Enemy(WIDTH/2, HEIGHT/2+200, player.rect.x, player.rect.y)
all_sprites.add(enemy)

#initialize the camera
camera_group = CameraGroup.CameraGroup()
camera_group.add(all_sprites)


#game loop 
while running:
    clock.tick(FPS) #FPS frames per second
    #get all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update the game
    all_sprites.update()
    enemy.update_player_position(player.rect.x, player.rect.y)
    #draw the screen
    #screen.fill(WHITE)
    camera_group.custom_draw(player)
    pygame.display.update()

pygame.quit()