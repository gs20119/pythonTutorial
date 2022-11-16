
from cs1robots import *
load_world('worlds/hurdles1.wld')
gshs = Robot()
gshs.set_trace('blue')

###########################################

def hurdle(robot):
    robot.turn_left_move()
    robot.turn_right_move()
    robot.turn_right_move()
    robot.turn_left_move()

gshs.move()
for i in range(4): hurdle(gshs)

###########################################


