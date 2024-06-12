import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #Movement attributes  
        self.x_change = 0
        self.y_change = 0
        self.max_speed = 5
        self.speed_resistance = 0.9
    
        #Attributes
        self.health = 100
        self.level = 1

    def update(self):
       #update the robot's position
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        #limit the robot's speed
        vector_length = (self.x_change ** 2 + self.y_change ** 2) ** 0.5
        if vector_length > self.max_speed:
            self.x_change = self.x_change / vector_length * self.max_speed
            self.y_change = self.y_change / vector_length * self.max_speed

        #slow the robot down
        self.x_change *= self.speed_resistance
        self.y_change *= self.speed_resistance
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        #move the robot smoothly with acceleration
        self.x_change += dx
        self.y_change += dy

            
        
