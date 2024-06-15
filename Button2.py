import pygame

class Button2:
    def __init__(self, x, y, width, height, text, font, color, hover_color, text_color, action=None, *args, **kwargs):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.action = action
        self.is_clicked = False
        #if the button has a value, it will be passed to the action function
        for key, value in kwargs.items():
            self.value = value
        

    def draw(self, screen, window_offset=(0,0)):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        offset_x, offset_y = window_offset
        mouse_pos = (mouse_x - offset_x, mouse_y - offset_y)
        mouse_click = pygame.mouse.get_pressed()

        #print("TT",mouse_pos ," Button1:)",self.rect.topleft[0])
     
        if self.rect.collidepoint(mouse_pos):
            #print("Button2:)",screen.get_rect().topleft[0])
            pygame.draw.rect(screen, self.hover_color, self.rect)
            if mouse_click[0] == 1 and self.action and not self.is_clicked:
                self.action()
                #print("Button clicked")
                self.is_clicked = True
            elif mouse_click[0] == 0:
                self.is_clicked = False

        else:
            pygame.draw.rect(screen, self.color, self.rect)

        if self.font:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)


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
    