import pygame
import Robot, Bullet
import Robot2

class Player(Robot2.Robot2):
    def __init__(self, x, y):
        super().__init__(x, y)
        # self.image.fill((0, 255, 255))
        
        #Attributes
        self.speed = 50
        self.max_speed = 500
        self.health = 100
        self.level = 1
        self.max_health = 100 

        self.attack = 30
        self.max_bullets = 10
        self.bullets = 10
        self.bullet_speed = 10
        self.bullet_cooldown = 300
        self.health_bar_size = [50, 10]

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

    def draw(self, screen, offset):
        super().draw(screen, offset)

    def shoot(self):
        #print("Shooting")
        #shoot a bullet in the direction the mouse is pointing
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        direction = direction.normalize()
        if self.bullets > 0 or 1: #infinte bullets
            bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, self.bullet_speed, direction)
            self.bullets -= 1
            #print("Bullets: ", direction)
            return bullet
        
    def move(self, dx, dy):
        return super().move(dx, dy)