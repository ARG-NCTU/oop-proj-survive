from Enemy import Enemy
from Player import Player
import pygame

def test_enemy_initialization():
    pygame.init()
    player = Player(0, 0)
    enemy = Enemy(0, 0, 0, player)
    assert enemy.body.position.x == 0
    assert enemy.body.position.y == 0

def test_enemy_move():
    pygame.init()
    player = Player(0, 0)
    enemy = Enemy(0, 0, 0, player)
    enemy.move(10, 20)
    assert enemy.body.velocity.x == 10
    assert enemy.body.velocity.y == 20

def test_enemy_covert_xy_to_pygame():
    pygame.init()
    player = Player(0, 0)
    enemy = Enemy(0, 0, 0, player)
    pygame_x, pygame_y = enemy.covert_xy_to_pygame(100, 200)
    assert pygame_x == 100
    assert pygame_y == 1800

def test_enemy_convert_xy_to_pymunk():
    pygame.init()
    player = Player(0, 0)
    enemy = Enemy(0, 0, 0, player)
    pymunk_x, pymunk_y = enemy.convert_xy_to_pymunk(100, 200)
    assert pymunk_x == 100
    assert pymunk_y == 1800

def test_enemy_shoot():
    pygame.init()
    player = Player(0, 0)
    enemy = Enemy(0, 0, 0, player)
    enemy.ready_to_shoot = True
    bullet = enemy.shoot()
    assert bullet.rect.centerx == enemy.rect.centerx
    assert bullet.rect.centery == enemy.rect.centery


