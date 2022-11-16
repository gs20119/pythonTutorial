
from cs1robots import *
create_world(20,20)
gshs = Robot(beepers=10000)
gshs.set_pause(0.1)

def left(robot): robot.turn_left()

def right(robot):
    for i in range(3): left(robot)

def around(robot):
    for i in range(2): left(robot)

def home(robot):
    goto(robot, 1, 1)
    clear_beeper_trace(gshs)

def goto(robot, X, Y):
    x, y = robot.get_pos()
    Y -= y
    X -= x
    while not robot.facing_north(): left(robot)
    if Y<0: around(robot)
    for i in range(abs(Y)): robot.move()
    while not robot.facing_north(): left(robot)
    (right if X>0 else left)(robot)
    for i in range(abs(X)): robot.move()

###########################################

from random import shuffle
n       = 20
trials  = 1000
dead    = 0
sum     = 0
movement = [(1,0),(0,1),(-1,0),(0,-1)]

###########################################

for t in range(trials):
    a = [[False for i in range(n+2)] for j in range(n+2)]
    x, y = 1+n//2, 1+n//2
    gshs.set_trace('blue')
    while (1 <= x <= n) and (1 <= y <= n):
        if a[x][y]:
            dead += 1
            home(gshs)
            break
        goto(gshs, x, y)
        gshs.drop_beeper()
        a[x][y] = True
        shuffle(movement)
        for i, j in movement:
            if not a[x+i][y+j]:
                x, y = x+i, y+j
                break
    home(gshs)

###########################################

print(str(100*dead/trials) + '% dead ends')