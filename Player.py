import pygame
import Robot, Bullet
import Robot2
import Setting as s
import math

class Player(Robot2.Robot2):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add frame to the circle
        pygame.draw.circle(self.image, (100, 100, 100), (25, 25), 25, 3)
        # self.image.fill((0, 255, 255))
        
        #Attributes
        self.speed = 50
        self.max_speed = 500
        self.health = 200
        self.level = 1
        self.max_health = 200 

        self.attack = 30
        self.max_bullets = 10
        self.bullets = 10
        self.bullet_speed = 10
        self.bullet_cooldown = 300
        self.health_bar_size = [50, 10]

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
        if self.bullets==0:
            if self.bullet_cooldown > 0:
                self.bullet_cooldown -= 1
            else:
                self.bullets = 10
                self.bullet_cooldown = 300
        if pygame.time.get_ticks() % 10000 == 0:
            self.level_up()


        # mouse_pos = pygame.mouse.get_pos()
        # direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        # print("Player: ", self.rect.x, self.rect.y,"Bullets: ", direction)
        

    def draw(self, screen):

        self.draw_barrel(screen, 0)

        if 1: #for testing
            self.draw_barrel(screen, 90)
            self.draw_barrel(screen, 180)
            self.draw_barrel(screen, 270)
            
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
        self.level += 1
        self.max_health += 10
        if self.health + 10 <= self.max_health:
            self.health += 10
        self.attack += 5
        self.bullets += 5
        self.max_bullets += 5
        self.bullet_speed += 2
        self.speed += 5
        self.max_speed += 10

    def shoot(self):
        #shoot a bullet in the direction the mouse is pointing
        sub_bullets = []
        direction = self.get_mouse_direction()
        bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, self.bullet_speed, direction)
        sub_bullets.append(bullet)
        if 1: #for testing
            for i in [90, 180, 270]:
                direction = self.get_mouse_direction().rotate(i)
                bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, self.bullet_speed, direction)
                sub_bullets.append(bullet)
        
        return sub_bullets
        # if self.bullets > 0 or 1: #infinte bullets
        #     bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, self.bullet_speed, direction)
        #     self.bullets -= 1
        #     return bullet
        
    def move(self, dx, dy):
        return super().move(dx, dy)
    
    def get_mouse_direction(self):
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos[0] - s.scrWIDTH/2 , mouse_pos[1] - s.scrHEIGHT/2)
        direction = direction.normalize()
        return direction