
from cs1robots import *
from random import randint
load_world('worlds/finalMaze2.wld')
orient_dict = {0:'N', 1: 'E', 2: 'S', 3: 'W'}

gshs1 = Robot(color="light_blue", orientation=orient_dict[randint(0,3)], avenue=11, street=11)
gshs1.set_trace(color='blue')
gshs1.set_pause(1)

gshs2 = Robot(color="yellow", orientation=orient_dict[randint(0,3)], avenue=11, street=11)
gshs2.set_trace(color='blue')
gshs2.set_pause(1)

def left(robot):
    robot.turn_left()

def right(robot):
    for i in range(3): left(robot)

def around(robot):
    for i in range(2): robot.turn_left()

def move(robot):
    if not robot.front_is_clear(): around(robot)
    robot.move()

############################################

command = []
with open("commands/command.txt", "r") as f: # with = 리소스를 잠시 사용한 후 반납
    for i, line in enumerate(f):
        command.append(line.rstrip('\n'))

print(command[0] + " " + command[1])

############################################

def isCircular(x, y, paths, robot):
    for c in [c for path in paths for c in path]:
        (move if c=='M' else right if c=='R' else left)(robot)
    pos = robot.get_pos()
    if pos[0]==x and pos[1]==y: return True
    return False

print(isCircular(11,11, [command[0]], gshs1))
print(isCircular(11,11, [command[1]], gshs2))

############################################

