import pygame
import Setting as s

class Button2:
    def __init__(self, x, y, width, height, text, font=None, color=(0, 0, 0), hover_color=(100, 100, 100), text_color=(255, 255, 255), action=None, *args, **kwargs):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.is_button_abled = True
        if self.font is None:
            self.font = pygame.font.Font(None, 30)  # Set default font size to 30
        self.text_color = text_color
        self.action = action
        self.is_clicked = False
        #if the button has a value, it will be passed to the action function
        for key, value in kwargs.items():
            self.value = value
        

    def draw(self, screen, window_offset=(0,0)):

        if not self.is_button_abled:
            pygame.draw.rect(screen, s.button_color_disabled, self.rect)
            pygame.draw.rect(screen, s.button_text_color_disabled, (self.rect.topleft[0] + 6, self.rect.topleft[1] + 2, 3, 11))
            pygame.draw.rect(screen, s.button_text_color_disabled, (self.rect.topleft[0] + 2, self.rect.topleft[1] + 6, 11, 3))

            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        offset_x, offset_y = window_offset
        mouse_pos = (mouse_x - offset_x, mouse_y - offset_y)
        mouse_click = pygame.mouse.get_pressed()

        #print("TT",mouse_pos ," Button1:)",self.rect.topleft[0])
     
        if self.rect.collidepoint(mouse_pos):
            #print("Button2:)",screen.get_rect().topleft[0])      
            #draw the button with hover color
            pygame.draw.rect(screen, self.hover_color, self.rect)
            pygame.draw.rect(screen, s.button_text_color_hover, (self.rect.topleft[0] + 6, self.rect.topleft[1] + 2, 3, 11))
            pygame.draw.rect(screen, s.button_text_color_hover, (self.rect.topleft[0] + 2, self.rect.topleft[1] + 6, 11, 3))
        
            if mouse_click[0] == 1:
                pygame.draw.rect(screen, s.button_color_click, self.rect)
                pygame.draw.rect(screen, s.button_text_color_click, (self.rect.topleft[0] + 6, self.rect.topleft[1] + 2, 3, 11))
                pygame.draw.rect(screen, s.button_text_color_click, (self.rect.topleft[0] + 2, self.rect.topleft[1] + 6, 11, 3))
                if self.action and not self.is_clicked:
                    self.action()
                self.is_clicked = True
            elif mouse_click[0] == 0:
                self.is_clicked = False
            

        else:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, s.button_text_color, (self.rect.topleft[0] + 6, self.rect.topleft[1] + 2, 3, 11))
            pygame.draw.rect(screen, s.button_text_color, (self.rect.topleft[0] + 2, self.rect.topleft[1] + 6, 11, 3))

        # if self.font:
        #     text_surface = self.font.render(self.text, True, self.text_color)
        #     text_rect = text_surface.get_rect(center=self.rect.center)
        #     screen.blit(text_surface, text_rect)


# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     clock = pygame.time.Clock()

#     button = Button2(100, 100, 200, 50, "Click me", pygame.font.Font(None, 50), (0, 255, 0), (0, 200, 0), (0, 0, 0), lambda: print("Button clicked"))

#     running = True
#     while running:
#         screen.fill((255, 255, 255))
#         button.draw(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         pygame.display.flip()
#         clock.tick(60)
    