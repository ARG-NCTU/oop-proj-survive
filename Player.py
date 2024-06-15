import pygame
import Robot, Bullet
import Robot2
import Setting as s
import math
import pymunk
import SoundsManager

class Player(Robot2.Robot2):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add frame to the circle
        
        # self.image.fill((0, 255, 255))

        self.sounds_manager = SoundsManager.SoundsManager()
        
        #Attributes
        self.speed = 50
        self.max_speed = 500
        self.health = 200
        self.level = 1
        self.max_level = 30
        self.max_health = 200 
        self.gun_level = 1
        self.talent_point = 3

        self.attack = 30
        self.max_bullets = 10
        self.bullets = 10
        self.bullet_speed = 10
        self.bullet_reload = 30
        self.bullet_reload_max = 35
        self.bullet_cooldown = 5
        self.bullet_cooldown_max = 7
        self.ready_to_shoot = True
        self.superlevel = 1

        self.barrel_amout = [1,2,4,5,6,7,8]
        self.gunlevel_to_bullet = {
            "bullet_speed":[1,0,0,1,0,0],
            "bullet_reload":[0,-1,0,-1,0,-1],
            "bullet_cooldown":[-1,0,-1,0,-1,0],
            "max_bullets":[1,1,1,1,1,1],
        }

        self.health_bar_size = [50, 10]
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 150, 0))
        self.image.set_colorkey((255, 150, 0))
        self.rect = self.image.get_rect()
        self.radius = 25
        pygame.draw.circle(self.image, (255, 200, 0), (25, 25), 25)
        pygame.draw.circle(self.image, (100, 100, 100), (25, 25), 25, 3)
        self.rect.center = self.covert_xy_to_pygame(x, y)
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 1
        

        #barrel of the gun
        barrel_length = 50
        barrel_width = 30
        self.barrel = pygame.Surface((barrel_length, barrel_width))
        self.barrel.fill((70, 70, 70))
        pygame.draw.rect(self.barrel, (100, 100, 100), (0, 0, barrel_length, barrel_width), 3) # draw the frame of the barrel
        self.barrel.set_colorkey((0, 0, 0))

    def draw_health_bar(self, screen):
        self.health_bar_position = [self.rect.x, self.rect.y-25]  
        # Draw the background of the health bar
        pygame.draw.rect(screen, (255,0,0), (*self.health_bar_position, *self.health_bar_size))
        #Draw the health on top of the background
        pygame.draw.rect(screen, (0,255,0), (*self.health_bar_position, int(self.health / self.max_health * self.health_bar_size[0]), self.health_bar_size[1]))
    
    def update(self):
        super().update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            super().move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            super().move(self.speed, 0)
        if keys[pygame.K_UP]:
            super().move(0, self.speed)
        if keys[pygame.K_DOWN]:
            super().move(0, -self.speed)
        self.draw_health_bar(pygame.display.get_surface())
        #reload the bullets
        if self.bullets==0:
            if self.bullet_reload > 0:
                self.bullet_reload -= 1
            else:
                self.bullets = self.max_bullets
                self.bullet_reload = self.bullet_reload_max

        # initial ready to shoot
        if self.ready_to_shoot == False:
            if self.bullet_cooldown > 0:
                self.bullet_cooldown -= 1
            else:
                self.ready_to_shoot = True
                self.bullet_cooldown = self.bullet_cooldown_max


        # mouse_pos = pygame.mouse.get_pos()
        # direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        # print("Player: ", self.rect.x, self.rect.y,"Bullets: ", direction)
        

    def draw(self, screen):
        #draw the barrel of the gun
        current_barrel = self.barrel_amout[self.superlevel-1]
        for i in range(0, current_barrel):
            self.draw_barrel(screen, i*360/current_barrel)

        # if self.level >= 5: #for testing
        #     self.draw_barrel(screen, 180)
        # if self.level >= 10 :
        #     self.draw_barrel(screen, 90)
        #     self.draw_barrel(screen, 270)
            
        #draw the player
        super().draw(screen)     

    def draw_barrel(self, screen, origin_angle):
        #draw the barrel of the gun
        angle = math.degrees(math.atan2(self.get_mouse_direction().y, self.get_mouse_direction().x)) + origin_angle
        rect = self.barrel.get_rect()
        old_center = rect.center
        new_barrel = pygame.transform.rotate(self.barrel, -angle)
        rect = new_barrel.get_rect()
        rect.center = old_center
        #offset the barrel to the center of the player with the angle
        offset = pygame.math.Vector2(25,0).rotate(angle)
        screen.blit(new_barrel, (self.rect.centerx - rect.width/2, self.rect.centery - rect.height/2) + offset)
        
    def level_up(self):

        if self.level >= self.max_level: return
        # if self.level < 20: #max level=20
        #     self.level += 1
        #     if self.level % 5 == 0:
        #         self.max_health += 10
        #         if self.health + 10 <= self.max_health:
        #             self.health += 10
        #     elif self.level % 5 == 1:
        #         self.attack += 3
        #     elif self.level % 5 == 2:
        #         self.bullets += 3
        #         self.max_bullets += 3
        #     elif self.level % 5 == 3:
        #         self.bullet_speed += 1
        #         self.speed += 2
        #         self.max_speed += 2
        #     else:
        #         if self.bullet_reload_max >= 1:
        #             self.bullet_reload_max -= 1

        self.level += 1
        self.talent_point += 1
        if self.level % 5 == 0:
            self.superlevel += 1
            self.sounds_manager.superlevel_up_sound.play()
        else:
            self.sounds_manager.level_up_sound.play()

    def shoot(self):
        if self.ready_to_shoot and self.bullets > 0:
            self.ready_to_shoot = False
            self.bullets -= 1  
            #shoot a bullet in the direction the mouse is pointing
            sub_bullets = []
            
            
            current_barrel = self.barrel_amout[self.superlevel-1]
            for i in range(0, current_barrel):
                direction = self.get_mouse_direction().rotate(i*360/current_barrel)
                bullet = Bullet.Bullet(self.rect.centerx+direction.x*50, self.rect.centery+direction.y*50, self.bullet_speed, direction)
                sub_bullets.append(bullet)

            return sub_bullets
        
    def move(self, dx, dy):
        return super().move(dx, dy)
    
    def get_mouse_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos[0] - s.scrWIDTH/2 , mouse_pos[1] - s.scrHEIGHT/2)
        try:
            direction = direction.normalize()
        except:
            direction = pygame.math.Vector2(0,0)
        return direction
    
    def add_max_health(self):
        self.talent_point -= 1
        rate = self.health/self.max_health
        self.max_health += 20
        self.health = int(self.max_health * rate)

    
    def add_attack(self):
        self.talent_point -= 1
        self.attack += 3

    def add_speed(self):
        self.talent_point -= 1
        self.speed += 2
        self.max_speed += 2

    def add_gun_level(self):
        self.talent_point -= 1
        self.gun_level += 1

        self.bullet_speed += self.gunlevel_to_bullet["bullet_speed"][(self.gun_level-1)%6]
        self.bullet_reload += self.gunlevel_to_bullet["bullet_reload"][(self.gun_level-1)%6]
        self.bullet_reload_max = max(0, self.bullet_reload_max)
        self.bullet_cooldown += self.gunlevel_to_bullet["bullet_cooldown"][(self.gun_level-1)%6]
        self.bullet_cooldown_max = max(0, self.bullet_cooldown_max)
        self.max_bullets += self.gunlevel_to_bullet["max_bullets"][(self.gun_level-1)%6]
        # self.bullet_reload_max -= 1
        # self.bullet_reload_max = max(0, self.bullet_reload_max)
        # self.bullet_cooldown_max -= 1
        # self.bullet_cooldown_max = max(0, self.bullet_cooldown_max)
        # self.bullet_speed += 1
        # self.max_bullets += 1

    def reset(self):
        self.speed = 50
        self.max_speed = 500
        self.health = 200
        self.level = 1
        self.max_level = 30
        self.max_health = 200 
        self.gun_level = 1
        self.talent_point = 2

        self.attack = 30
        self.max_bullets = 10
        self.bullets = 10
        self.bullet_speed = 10
        self.bullet_reload = 30
        self.bullet_reload_max = 35
        self.bullet_cooldown = 5
        self.bullet_cooldown_max = 7
        self.ready_to_shoot = True
        self.superlevel = 1

        