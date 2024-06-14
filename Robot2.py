import pygame, pymunk
import Setting as s

class Robot2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #pygame
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 150, 0))
        self.image.set_colorkey((255, 150, 0))
        self.rect = self.image.get_rect()
        self.radius = 25
        pygame.draw.circle(self.image, (255, 200, 0), (25, 25), 25)
        self.rect.center = self.covert_xy_to_pygame(x, y)

        #pymunk
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = 0, 0
        self.shape = pymunk.Circle(self.body, 25)
        self.shape.density = 1
        self.shape.elasticity = 1
        #space.add(self.body, self.shape)
        self.shape.collision_type = 1


        #Movement attributes  
        self.x_change = 0
        self.y_change = 0
        self.max_speed = 300
        self.speed_resistance = 0.9
    
        #Attributes
        self.health = 100
        self.level = 1

    def update(self):
        pass
        #update the robot's position
        self.rect.center = self.covert_xy_to_pygame(self.body.position.x, self.body.position.y)
    
        #limit the robot's speed
        speed = self.body.velocity.length
        if speed > self.max_speed:
            self.body.velocity = self.body.velocity.normalized() * self.max_speed

        # slow the robot down
        self.body.velocity *= self.speed_resistance
        

    def draw(self, screen):
        x = self.rect.x
        y = self.rect.y
        screen.blit(self.image, (x, y))
        pass

    def move(self, dx, dy):
        pass
        #move the robot smoothly with acceleration
        self.body.velocity += dx, dy

    def covert_xy_to_pygame(self, x, y):
        return x, s.HEIGHT - y
    
    def convert_xy_to_pymunk(self, x, y):
        return x, s.HEIGHT - y

            
        