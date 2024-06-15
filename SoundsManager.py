import pygame
import random

class SoundsManager:
    def __init__(self):
        self.damage_sound = pygame.mixer.Sound("sounds/damaged4.mp3")
        self.shoot_sound = pygame.mixer.Sound("sounds/pop.mp3")
        self.supply_sound = pygame.mixer.Sound("sounds/powerup03.mp3")
        self.kill_ememy_sound = pygame.mixer.Sound("sounds/damaged5.mp3")
        self.level_up_sound = pygame.mixer.Sound("sounds/levelup1.mp3")
        self.superlevel_up_sound = pygame.mixer.Sound("sounds/levelup2.mp3")
        self.button_sound = pygame.mixer.Sound("sounds/button.mp3")
        self.talent_sound = pygame.mixer.Sound("sounds/talentpoint.mp3")
        self.gameover_sound = pygame.mixer.Sound("sounds/gameover.mp3")