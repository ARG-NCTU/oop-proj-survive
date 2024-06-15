import random
import pygame
import Robot, Enemy, CameraGroup, Bullet, Player, Wall, Supply, Button
import pymunk
import RankManager, SoundsManager, StatusWindow
import time
import Setting as s

### Note that the coordinates follow the pymunk coordinate system
### where (0, 0) is at the bottom left corner of the screen



#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((s.scrWIDTH, s.scrHEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
minutes = 0
seconds = 0
running = True
start_page_running = True
end_page_running = True
#initialize the pymunk
space = pymunk.Space()

#initialize the robot
all_sprites = pygame.sprite.Group()
player = Player.Player(400, 1600)
space.add(player.body, player.shape)
all_sprites.add(player)

score = 0
score_change = False
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

#initialize the supplies
supplies = pygame.sprite.Group()

#initialize the walls
wall_left = Wall.Wall([s.LEFT, s.TOP], [s.LEFT, s.BOTTOM],2)
wall_right = Wall.Wall((s.RIGHT, s.TOP), (s.RIGHT, s.BOTTOM),2)
wall_top = Wall.Wall((s.LEFT, s.TOP), (s.RIGHT, s.TOP),2)
wall_bottom = Wall.Wall((s.LEFT, s.BOTTOM), (s.RIGHT, s.BOTTOM),2)
space.add(wall_left.body, wall_left.shape)
space.add(wall_right.body, wall_right.shape)
space.add(wall_top.body, wall_top.shape)
space.add(wall_bottom.body, wall_bottom.shape)

start_button = Button.Button(300, 500, 200, 50, (255, 0, 0), 'Start')

#RankManager
rank_manager = RankManager.RankManager()

#initialize sounds effects
sounds_manager = SoundsManager.SoundsManager()

#Status window
status_window = StatusWindow.StatusWindow(player)

while start_page_running:
    screen.fill((255, 255, 255))  
    #Draw a circle
    start_button.draw(screen)
    pygame.draw.circle(screen, (155, 0, 0), (25, 25), 25)
    pygame.draw.circle(screen, (255, 0, 0), (25, 25), 15)
    pygame.draw.circle(screen, (0, 155, 0), (100, 35), 25)
    pygame.draw.circle(screen, (0, 255, 0), (100, 35), 15)
    pygame.draw.circle(screen, (0, 0, 155), (35, 100), 25)
    pygame.draw.circle(screen, (0, 0, 255), (35, 100), 15)
    #Draw a rectangle
    pygame.draw.rect(screen, (155, 155, 0), (650, 700, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (665, 715, 20, 20))
    pygame.draw.circle(screen, (255, 200, 0), (750, 650), 25)
    font = pygame.font.Font(None, 55)  
    text = font.render("My Game", True, (0, 0, 0))  
    screen.blit(text, (300, 200))  
    pygame.display.flip()  # 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.is_clicked(pygame.mouse.get_pos()):
                start_time = pygame.time.get_ticks()
                start_page_running = False


#game loop 
while running:
    
   # print(time.strftime("%Y/%m/%d\n%H:%M:%S", time.localtime()))
    #----------------------------------------------
    #get all the events
    #----------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #hold the mouse button to shoot
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
                # sub_bullets = player.shoot()
                # all_sprites.add(bullet for bullet in sub_bullets)
                # camera_group.add(bullet for bullet in sub_bullets)
                # bullets.add(bullet for bullet in sub_bullets)

    #----------------------------------------------
    #update the game
    #----------------------------------------------
    all_sprites.update()
    status_window.update()

    #if mouse is pressed, shoot
    if pygame.mouse.get_pressed()[0]:
        sub_bullets = player.shoot()
        if sub_bullets:
            sounds_manager.shoot_sound.play()
            all_sprites.add(bullet for bullet in sub_bullets)
            camera_group.add(bullet for bullet in sub_bullets)
            bullets.add(bullet for bullet in sub_bullets)

    for enemy in enemies:
        if enemy.check_attack(bullets): # The enemy is dead
            enemy_number -=1 
            score_change = True
            space.remove(enemy.body, enemy.shape)
       
        score += enemy.score
        if enemy.enemytype == 3 and pygame.time.get_ticks() % 1000 < 10:
            enemy_bullet = enemy.shoot()
            if enemy_bullet:
                all_sprites.add(enemy_bullet)
                camera_group.add(enemy_bullet)
                enemy_bullets.add(enemy_bullet)
        if enemy.enemytype == 7 and pygame.time.get_ticks() % 1000 < 20:
            enemy_bullet = enemy.shoot()
            if enemy_bullet:
                all_sprites.add(enemy_bullet)
                camera_group.add(enemy_bullet)
                enemy_bullets.add(enemy_bullet)
    
    for enemy_bullet in enemy_bullets:
        if pygame.sprite.collide_circle(player, enemy_bullet):
            sounds_manager.damage_sound.play()
            enemy_bullet.kill()
            player.health -= 10
    if player.health <= 0:
        running = False 

    if pygame.time.get_ticks() % 2000 <= 10:
        max_enemies += 1

    #enemy 死掉的时候，重新生成一个enemy
    if enemy_number < max_enemies and pygame.time.get_ticks() % 1000 < 100:
        if minutes * 60 + seconds < 20:
            enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(0, 3),player)
        elif minutes * 60 + seconds < 40:
            enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(1, 4),player)
        elif minutes * 60 + seconds < 60:
            enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(2, 5),player)
        elif minutes * 60 + seconds < 80:
            enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(3, 6),player)
        else:
            enemy = Enemy.Enemy(random.randint(50, 1950), random.randint(50, 1950), random.randint(4, 7),player)

        enemies.add(enemy)
        space.add(enemy.body, enemy.shape)
        all_sprites.add(enemy)
        camera_group.add(enemy)
        enemy_number += 1
    #create a boss
    for enemy in enemies:
        if enemy.enemytype == 8:
            has_boss = True
            break
        else:
            has_boss = False
    if  seconds % 20 == 19 and not has_boss:
        enemy = Enemy.Enemy(random.randint(200, 1800), random.randint(200, 1800), 8,player)
        enemies.add(enemy)
        space.add(enemy.body, enemy.shape)
        all_sprites.add(enemy)
        camera_group.add(enemy)
        has_boss = True

    #create a supply every 5 seconds
    if pygame.time.get_ticks() % 5000 <= 10:
        supply = Supply.Supply(random.randint(50, 1950), random.randint(50, 1950), random.randint(0, 2))
        supplies.add(supply)
        all_sprites.add(supply)
        camera_group.add(supply)
    for supply in supplies:
        if pygame.sprite.collide_circle(player, supply):
            supply.kill()
            sounds_manager.supply_sound.play()
            if supply.supplytype == 0:
                if player.health + 30 <= player.max_health:
                    player.health += 30
                elif player.health < player.max_health:
                    add_health = player.max_health - player.health
                    player.health += add_health
            elif supply.supplytype == 1:
                if player.speed +30 <= player.max_speed:
                    player.speed += 30
                elif player.speed < player.max_speed:
                    add_spped = player.max_speed - player.speed
                    player.speed += add_spped
            elif supply.supplytype == 2:
                player.attack += 10

    current_time = pygame.time.get_ticks()-start_time
    minutes = current_time // 60000
    seconds = (current_time % 60000) // 1000

    #----------------------------------------------
    # Draw the screen
    #----------------------------------------------
    screen.fill((255,0,0))
    camera_group.temp_surface.fill((255,255,255))
    camera_group.draw_ground()
    
    if score % 5 == 0 and score != 0 and score_change:
        player.level_up()
        score_change = False

    player.draw_health_bar(camera_group.temp_surface)
    for enemy in enemies:
        enemy.draw_health_bar(camera_group.temp_surface)


    # Draw the walls
    wall_left.draw(camera_group.temp_surface,"left")
    wall_right.draw(camera_group.temp_surface, "right")
    wall_top.draw(camera_group.temp_surface,"top")
    wall_bottom.draw(camera_group.temp_surface,"bottom")
    # Draw the sprites
    camera_group.custom_draw(player)
    # Draw the status window
    status_window.draw(screen)

    font = pygame.font.Font(None, 55) # Choose the font for the score, None means the default font
    text = font.render("Score: " + str(score), 10, (0, 0, 0)) # Create the text
    screen.blit(text, (20,20)) # Draw the text on the screen at position (20, 20)
    time_text= font.render("Time: " + str(minutes) + ":" + str(seconds).zfill(2), 10, (0, 0, 0))
    screen.blit(time_text, (20, 50))
    level_text = font.render("Level: " + str(player.level), 10, (0, 0, 0))
    screen.blit(level_text, (20, 80))
    #player.draw(screen)
    #all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(s.FPS) #FPS frames per second
    space.step(1/s.FPS) # Step the physics simulation

while end_page_running:
    screen.fill((255, 255, 255))  
    #Draw a circle
    pygame.draw.circle(screen, (155, 0, 0), (25, 25), 25)
    pygame.draw.circle(screen, (255, 0, 0), (25, 25), 15)
    pygame.draw.circle(screen, (0, 155, 0), (100, 35), 25)
    pygame.draw.circle(screen, (0, 255, 0), (100, 35), 15)
    pygame.draw.circle(screen, (0, 0, 155), (35, 100), 25)
    pygame.draw.circle(screen, (0, 0, 255), (35, 100), 15)
    #Draw a rectangle
    pygame.draw.rect(screen, (155, 155, 0), (650, 700, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (665, 715, 20, 20))
    pygame.draw.circle(screen, (255, 200, 0), (750, 650), 25)
    font = pygame.font.Font(None, 55)  
    text = font.render("Game Over", True, (0, 0, 0))  
    screen.blit(text, (300, 200))  
    kill = font.render("Kill: " + str(score), 10, (0, 0, 0)) # Create the text
    screen.blit(kill, (300,250)) # Draw the text on the screen at position (20, 20)
    time_text= font.render("Time: " + str(minutes) + ":" + str(seconds).zfill(2), 10, (0, 0, 0))
    screen.blit(time_text, (300, 300))
    final_score = font.render("Final Score: " + str(score * (minutes*60 + seconds)), 10, (0, 0, 0))
    screen.blit(final_score, (300, 350))
    pygame.display.flip()  # 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_page_running = False

# store the score
current_time = time.strftime("%Y/%m/%d\n%H:%M:%S", time.localtime())
rank_manager.add_data(current_time, score, minutes*60 + seconds, score * (minutes*60 + seconds))
rank_manager.show_rank()
pygame.quit()