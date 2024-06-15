import pygame
import Setting as s
import Button2

class StatusWindow(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.WINDOW_COLOR = (225,225,225)
        self.WINDOW_WIDTH = 140
        self.WINDOW_HEIGHT = 160
        self.image = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.image.fill(self.WINDOW_COLOR)
        #draw the frame of the window
        pygame.draw.rect(self.image, (200,200,200), (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 3)
        self.rect = self.image.get_rect(bottomright=(s.scrWIDTH - 10, s.scrHEIGHT - 10))

        self.text_lst = ["HP", "Attack", "Speed", "Gun level", "Talent point"]
        self.value_lst = [self.player.health, self.player.attack, self.player.speed, self.player.gun_level, self.player.talent_point]
        self.action_lst = [self.player.add_max_health, self.player.add_attack, self.player.add_speed, self.player.add_gun_level]
        #button color
        self.button_color = (100,100,100)
        self.button_color_hover = (150,150,150)
        self.button_color_click = (200,200,200)
        self.button_text_color = (255,255,255)
        self.button_text_color_hover = (205,205,205)
        self.button_text_color_click = (155,155,155)

        self.button_amount = len(self.text_lst) -1
        self.buttons = []
        for i in range(self.button_amount):
            button = Button2.Button2(113, 11 + 30 * i, 15, 15, None, None, self.button_color, self.button_color_hover, self.button_text_color, self.action_lst[i])
            self.buttons.append(button)
            


    def update(self):
        pass
        self.image.fill(self.WINDOW_COLOR)
        pygame.draw.rect(self.image, (200,200,200), (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 3)
        font = pygame.font.Font(None, 25)

        lst_len = len(self.text_lst)
        self.value_lst = [self.player.health, self.player.attack, self.player.speed, self.player.gun_level, self.player.talent_point]

        for i in range(lst_len):
            if self.text_lst[i] == "HP":
                value = f"{self.value_lst[i]}/{self.player.max_health}"
            else:
                value = self.value_lst[i]
            text = font.render(f"{self.text_lst[i]}: {value}", True, (0, 0, 0))
            self.image.blit(text, (10, 10 + 30 * i))
            # button = self.create_plus_button(self.image, value_lst[i], 113, 11 + 30 * i)

        for button in self.buttons:
            button.is_button_abled = self.player.talent_point > 0
            button.draw(self.image, self.rect.topleft)
        


    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    # def create_plus_button(self, screen, item, x, y):
    #     #create a plus button bside the item. when clicked, the item will be upgraded
    #     #draw the plus button
    #     button = pygame.Surface((15, 15))
    #     button.fill((100,100,100))
    #     #draw the plus sign on the center of the button
    #     pygame.draw.rect(button, (255, 255, 255), (6, 2, 3, 11))
    #     pygame.draw.rect(button, (255, 255, 255), (2, 6, 11, 3))

    #     screen.blit(button, (x, y))
    #     return button

    # def button_hover(self, button, mouse_pos):
    #     x, y = mouse_pos
    #     button_rect = button.get_rect()
    #     if button_rect.collidepoint(x, y):
    #         return True
    #     return False

    # def check_value_addable(self, value):
    #     pass
    #     return True

    # def add_value(self, value):
        
    #     value += 1
    #     print("value", value)
    #     return value
        