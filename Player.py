import pygame
import Robot, Bullet

class Player(Robot.Robot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((0, 255, 255))
        
        #Attributes
        self.speed = 2
        self.max_speed = 5
        self.health = 100
        self.level = 1

        self.attack = 10
        self.bullets = 10
        self.bullet_speed = 10
        self.bullet_cooldown = 500


    def update(self):
        super().update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            super().move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            super().move(self.speed, 0)
        if keys[pygame.K_UP]:
            super().move(0, -self.speed)
        if keys[pygame.K_DOWN]:
            super().move(0, self.speed)

    def draw(self, screen):
        super().draw(screen)

    def shoot(self):
        #print("Shooting")
        #shoot a bullet in the direction the mouse is pointing
        mouse_pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery)
        direction = direction.normalize()
        if self.bullets > 0:
            bullet = Bullet.Bullet(self.rect.centerx, self.rect.centery, self.bullet_speed, direction)
            self.bullets -= 1
            #print("Bullets: ", direction)
            return bullet
        
    def move(self, dx, dy):
        return super().move(dx, dy)