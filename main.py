import random
import pygame
import Robot, Enemy, CameraGroup, Bullet, Player
import pymunk

### Note that the coordinates follow the pymunk coordinate system
### where (0, 0) is at the bottom left corner of the screen

FPS = 60 #frames per second
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 800
scrWIDTH, scrHEIGHT = 800, 800

LEFT = 25
RIGHT = 775
TOP = 25
BOTTOM = 775
MIDDLEX = (LEFT + RIGHT) / 2
MIDDLEY = (TOP + BOTTOM) / 2


#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((scrWIDTH, scrHEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True

#initialize the pymunk
space = pymunk.Space()

#initialize the robot
all_sprites = pygame.sprite.Group()
player = Player.Player(WIDTH/2, HEIGHT/2)
space.add(player.body, player.shape)
all_sprites.add(player)

# Create a group for the enemies
enemies = pygame.sprite.Group()
enemy_number = 1 #number of enemies
max_enemies = 0 #maximum number of enemies
#first enemy
enemy = Enemy.Enemy(random.choice((random.randint(0, 200), random.randint(600, 800))), random.choice((random.randint(0, 200), random.randint(600, 800))), random.randint(0, 2), player)
enemies.add(enemy)
space.add(enemy.body, enemy.shape)
all_sprites.add(enemy)

#initialize the camera
camera_group = CameraGroup.CameraGroup()
camera_group.add(all_sprites)

# Create a group for bullets
bullets = pygame.sprite.Group()


#game loop 
while running:
    
    #get all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #shoot a bullet
            if event.button == 1:
                bullet = player.shoot()
                if bullet:
                    all_sprites.add(bullet)
                    camera_group.add(bullet)
                    bullets.add(bullet)

    
    #update the game
    all_sprites.update()

    for enemy in enemies:
        enemy_number = enemy.check_attack(bullets, enemy_number)
   
    
    #enemy 死掉的时候，重新生成一个enemy
    if enemy_number < max_enemies and pygame.time.get_ticks() % 1000 < 30:
        enemy = Enemy.Enemy(random.choice((random.randint(0, 200), random.randint(600, 800))), random.choice((random.randint(0, 200), random.randint(600, 800))), random.randint(0, 2), player)
        enemies.add(enemy)
        space.add(enemy.body, enemy.shape)
        all_sprites.add(enemy)
        camera_group.add(enemy)
        enemy_number += 1
    

    #draw the screen
    screen.fill((255,0,0))
    camera_group.temp_surface.fill((255,255,255))
    
    player.draw_health_bar(camera_group.temp_surface)
    for enemy in enemies:
        enemy.draw_health_bar(camera_group.temp_surface)
    camera_group.custom_draw(player)
    #player.draw(screen)
    #all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS) #FPS frames per second
    space.step(1/FPS) # Step the physics simulation

pygame.quit()