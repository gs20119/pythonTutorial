
from cs1robots import *
load_world('worlds/harvest1.wld')
gshs = Robot()
gshs.set_trace('blue')

###########################################

def harvest(robot):
    robot.move(5)
    robot.turn_left_move()
    robot.turn_left()
    robot.move(5)
    robot.turn_right_move()
    robot.turn_right()

gshs.move()
for i in range(3): harvest(gshs)

###########################################


