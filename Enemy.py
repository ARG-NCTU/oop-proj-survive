import pygame
import Robot2
import random
import Bullet
import SoundsManager
import pymunk

class Enemy(Robot2.Robot2):
    def __init__(self, x, y, enemytype, player):
        super().__init__(x, y)
        self.player = player
        self.score = 0 #score for the player
        self.player_x = 400
        self.player_y = 300
        self.enemytype = enemytype
        
        if self.enemytype <= 7 and self.enemytype >=0:
            self.health_bar_size = [50, 10]
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 150, 0))
            self.image.set_colorkey((255, 150, 0))
            self.rect = self.image.get_rect()
            self.radius = 25
            pygame.draw.circle(self.image, (255, 200, 0), (25, 25), 25)
            self.rect.center = self.covert_xy_to_pygame(x, y)
            self.shape = pymunk.Circle(self.body, 25)
        elif self.enemytype == 8:
            self.health_bar_size = [100, 10]
            self.image = pygame.Surface((100, 100))
            self.image.fill((255, 150, 0))
            self.image.set_colorkey((255, 150, 0))
            self.rect = self.image.get_rect()
            self.radius = 50
            pygame.draw.circle(self.image, (255, 200, 0), (50, 50), 50)
            self.rect.center = self.covert_xy_to_pygame(x, y)
            self.shape = pymunk.Circle(self.body, 50)
        else:
            self.health_bar_size = [200, 10]
            self.image = pygame.Surface((200, 200))
            self.image.fill((255, 150, 0))
            self.image.set_colorkey((255, 150, 0))
            self.rect = self.image.get_rect()
            self.radius = 75
            pygame.draw.circle(self.image, (255, 200, 0), (100, 100), 100)
            self.rect.center = self.covert_xy_to_pygame(x, y)
            self.shape = pymunk.Circle(self.body, 75)
        self.shape.density = 1
        self.shape.elasticity = 1
        self.shape.collision_type = 1

        self.sounds_manager = SoundsManager.SoundsManager()

        if self.enemytype == 0: #red enemy
            self.health = 100
            self.max_health = 100
            self.attack = 10
            pygame.draw.circle(self.image, (155, 0, 0), (25, 25), 25)
            pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 15)
            self.speed = 20
        elif self.enemytype == 1: #green enemy
            self.health = 40
            self.max_health = 40
            self.attack = 7
            pygame.draw.circle(self.image, (0, 155, 0), (25, 25), 25)
            pygame.draw.circle(self.image, (0, 255, 0), (25, 25), 15)
            self.speed = 40
        elif self.enemytype == 2: #blue enemy
            self.health = 150
            self.max_health = 150
            self.attack = 15
            pygame.draw.circle(self.image, (0, 0, 155), (25, 25), 25)
            pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 15)
            self.speed = 10
        elif self.enemytype == 3:  #固定式砲台
            self.health = 100
            self.max_health = 100
            self.attack = 10
            pygame.draw.rect(self.image, (155, 155, 0), (0, 0, 50, 50))
            pygame.draw.rect(self.image, (255, 255, 0), (10, 10, 30, 30))
            self.speed = 0
        elif self.enemytype == 4: #red enemy upgraded
            self.health = 150
            self.max_health = 150
            self.attack = 15
            pygame.draw.circle(self.image, (60, 0, 0), (25, 25), 25)
            pygame.draw.circle(self.image, (255, 0, 0), (25, 25), 15)
            pygame.draw.circle(self.image, (60, 0, 0), (25, 25), 5)
            self.speed = 10
        elif self.enemytype == 5: #green enemy upgraded
            self.health = 100
            self.max_health = 100
            self.attack = 10
            pygame.draw.circle(self.image, (0, 60, 0), (25, 25), 25)
            pygame.draw.circle(self.image, (0, 255, 0), (25, 25), 15)
            pygame.draw.circle(self.image, (0, 60, 0), (25, 25), 5)
            self.speed = 40
        elif self.enemytype == 6: #blue enemy upgraded
            self.health = 200
            self.max_health = 200
            self.attack = 20
            pygame.draw.circle(self.image, (0, 0, 60), (25, 25), 25)
            pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 15)
            pygame.draw.circle(self.image, (0, 0, 60), (25, 25), 5)
            self.speed = 20
        elif self.enemytype == 7: #砲台 upgraded
            self.health = 150
            self.max_health = 150
            self.attack = 15
            pygame.draw.rect(self.image, (60, 60, 0), (0, 0, 50, 50))
            pygame.draw.rect(self.image, (255, 255, 0), (10, 10, 30, 30))
            pygame.draw.rect(self.image, (60, 60, 0), (15, 15, 20, 20))
            self.speed = 0
        elif self.enemytype == 8: #boss
            self.health = 1500
            self.max_health = 1500
            self.attack = 50
            pygame.draw.circle(self.image, (0, 0, 0), (50, 50), 50)
            pygame.draw.circle(self.image, (150, 150, 150), (50, 50), 40)
            pygame.draw.circle(self.image, (0, 0, 0), (50, 50), 30)
            self.speed = 20
        else: #big boss
            self.health = 4000
            self.max_health = 4000
            self.attack = 100
            pygame.draw.circle(self.image, (70, 70, 70), (100, 100), 100)
            pygame.draw.circle(self.image, (180, 0, 0), (100, 100), 90)
            pygame.draw.circle(self.image, (0, 0, 0), (100, 100), 80)
            self.speed = 35
        
        
    def draw_health_bar(self, screen):
        self.health_bar_position = [self.rect.x, self.rect.y-25]  
        # Draw the background of the health bar
        pygame.draw.rect(screen, (255,0,0), (*self.health_bar_position, *self.health_bar_size))
        #Draw the health on top of the background
        pygame.draw.rect(screen, (0,255,0), (*self.health_bar_position, int(self.health / self.max_health * self.health_bar_size[0]), self.health_bar_size[1]))
    
    def update_player_position(self, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
    
    def shoot(self):
        direction = pygame.math.Vector2(self.player_x-self.rect.x,self.player_y-self.rect.y)
        #print("Bullets: ", direction)
        direction = direction.normalize()
        bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, 7, direction)
        bullet.image.fill((100, 100, 0))
        return bullet
    
    def update(self):
        super().update()
        if self.player_x != self.rect.x:
            direction_x = (self.player_x - self.rect.x)/abs(self.player_x - self.rect.x)
        else:
            direction_x = 0
        if self.player_y != self.rect.y:
            direction_y = (self.player_y - self.rect.y)/abs(self.player_y - self.rect.y)
        else:
            direction_y = 0
        if self.player_x == self.rect.x and self.player_y == self.rect.y:
            direction_x = random.randint(-3, 3)
            direction_y = random.randint(-3, 3)

        super().move(direction_x*self.speed, -direction_y*self.speed)
        self.draw_health_bar(pygame.display.get_surface())

        # Update player position for all enemies
        self.update_player_position(self.player.rect.x, self.player.rect.y)
       
        # Check if the enemy collides with the player
        if pygame.sprite.collide_circle(self, self.player):
            self.sounds_manager.damage_sound.play()
            # move the enemy away from the player
            self.move((self.rect.x - self.player.rect.x) * 25, (self.rect.y - self.player.rect.y) * -25)
            self.player.health -= self.attack
            if self.player.health <= 0:
                self.running = False

        

   
    def draw(self, screen):
        super().draw(screen)
        
    def Attacked(self, damage, bullet):
        #ceheck the circle if collides with the bullet
        if pygame.sprite.collide_circle(self, bullet):
            self.health -= damage
            bullet.kill()
    
    def check_attack(self, bullets): #return if the enemy is dead
        for bullet in bullets:
            #check if the enemy is dead or attacted
            self.Attacked(self.player.attack, bullet)
            if self.health <= 0:
                self.kill()
                self.sounds_manager.kill_ememy_sound.play()
                self.score += 1
                return True
        return False