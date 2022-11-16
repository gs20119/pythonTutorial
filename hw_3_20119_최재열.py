
from cs1robots import *
load_world('worlds/finalMaze.wld')
gshs = Robot()
gshs.set_trace(color='blue')

def right(robot):
    for _ in range(3): robot.turn_left()

def left(robot):
    robot.turn_left()

############################################

while not gshs.on_beeper():
    if gshs.right_is_clear():
        right(gshs)
    while not gshs.front_is_clear():
        left(gshs)
    gshs.move()

gshs.pick_beeper()

############################################


