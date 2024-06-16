from Player import Player
import pygame



def test_player_initialization():
    pygame.init()
    player = Player(0, 0)
    assert player.body.velocity.x == 0
    assert player.body.velocity.y == 0

def test_player_move():
    pygame.init()
    player = Player(0, 0)
    player.move(10, 5)
    assert player.body.velocity.x == 10
    assert player.body.velocity.y == 5

def test_player_shoot():
    pygame.init()
    player = Player(0, 0)
    player.ready_to_shoot = True
    sub_bullets = player.shoot()
    print(sub_bullets)
    

def test_player_level_up():
    pygame.init()
    player = Player(0, 0)
    player.level_up()
    assert player.level == 2

def test_player_reset():
    pygame.init()
    player = Player(0, 0)
    player.level_up()
    player.reset()
    assert player.level == 1
    assert player.health == 200

