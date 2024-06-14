import random
import pygame
import Robot, Enemy, CameraGroup, Bullet, Player, Wall
import pymunk

### Note that the coordinates follow the pymunk coordinate system
### where (0, 0) is at the bottom left corner of the screen

FPS = 60 #frames per second
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 2000, 2000
scrWIDTH, scrHEIGHT = 800, 800

LEFT = 25
RIGHT = WIDTH-25
TOP = 25
BOTTOM = HEIGHT-25
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
player = Player.Player(400, 1600)
space.add(player.body, player.shape)
all_sprites.add(player)

score = 0

# Create a group for the enemies
enemies = pygame.sprite.Group()
enemy_number = 1 #number of enemies
max_enemies = 5 #maximum number of enemies
#first enemy
enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(0, 2),player)
enemies.add(enemy)
space.add(enemy.body, enemy.shape)
all_sprites.add(enemy)

#initialize the camera
camera_group = CameraGroup.CameraGroup()
camera_group.add(all_sprites)

# Create a group for bullets
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

#initialize the walls
wall_left = Wall.Wall([LEFT, TOP], [LEFT, BOTTOM],2)
wall_right = Wall.Wall((RIGHT, TOP), (RIGHT, BOTTOM),2)
wall_top = Wall.Wall((LEFT, TOP), (RIGHT, TOP),2)
wall_bottom = Wall.Wall((LEFT, BOTTOM), (RIGHT, BOTTOM),2)
space.add(wall_left.body, wall_left.shape)
space.add(wall_right.body, wall_right.shape)
space.add(wall_top.body, wall_top.shape)
space.add(wall_bottom.body, wall_bottom.shape)

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
        score += enemy.score
        if enemy.enemytype == 3 and pygame.time.get_ticks() % 1000 < 5:
            enemy_bullet = enemy.shoot()
            if enemy_bullet:
                all_sprites.add(enemy_bullet)
                camera_group.add(enemy_bullet)
                enemy_bullets.add(enemy_bullet)
    
    for enemy_bullet in enemy_bullets:
        if pygame.sprite.collide_circle(player, enemy_bullet):
            enemy_bullet.kill()
            player.health -= 10
            
    #enemy 死掉的时候，重新生成一个enemy
    if enemy_number < max_enemies and pygame.time.get_ticks() % 1000 < 30:
        enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(0, 3),player)
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

    wall_left.draw(camera_group.temp_surface)
    wall_right.draw(camera_group.temp_surface)
    wall_top.draw(camera_group.temp_surface)
    wall_bottom.draw(camera_group.temp_surface)
    camera_group.custom_draw(player)

    font = pygame.font.Font(None, 55) # Choose the font for the score, None means the default font
    text = font.render("Score: " + str(score), 10, (0, 0, 0)) # Create the text
    screen.blit(text, (20,20)) # Draw the text on the screen at position (20, 20)
    #player.draw(screen)
    #all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS) #FPS frames per second
    space.step(1/FPS) # Step the physics simulation

pygame.quit()