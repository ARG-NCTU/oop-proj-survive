from Robot2 import Robot2

def test_robot2_initialization():
    robot = Robot2(0, 0)
    assert robot.body.position.x == 0
    assert robot.body.position.y == 0

def test_robot2_move():
    robot = Robot2(0, 0)
    robot.move(10, 20)
    assert robot.body.velocity.x == 10
    assert robot.body.velocity.y == 20

def test_robot2_covert_xy_to_pygame():
    robot = Robot2(0, 0)
    pygame_x, pygame_y = robot.covert_xy_to_pygame(100, 200)
    assert pygame_x == 100
    assert pygame_y == 1800

def test_robot2_convert_xy_to_pymunk():
    robot = Robot2(0, 0)
    pymunk_x, pymunk_y = robot.convert_xy_to_pymunk(100, 200)
    assert pymunk_x == 100
    assert pymunk_y == 1800