
from cs1robots import *
load_world('p2.wld')
reader = Robot()
x, y = 1, 1
h = [0]

def left(robot):
    robot.turn_left()

def right(robot):
    for _ in range(3): left(robot)

def around(robot):
    for _ in range(2): left(robot)

#################################################

def moveTop(robot, n=0):
    while not robot.facing_north(): left(robot)
    while robot.front_is_clear():
        if n > 0:
            n -= 1
            robot.drop_beeper()
        robot.move()

def moveBottom(robot):
    while not robot.facing_north(): left(robot)
    around(robot)
    while robot.front_is_clear(): robot.move()

################################################

while True:
    moveTop(reader)
    right(reader)
    if not reader.front_is_clear(): break
    reader.move()
    moveBottom(reader)
    h.append(reader.get_pos()[1])

print(h)

###############################################

N = len(h)
Ml, Mr, ans = [0], [N-1], []
for i in range(1,N): Ml.append(i if h[Ml[i-1]]<h[i] else Ml[i-1])
for i in range(N-1): Mr.insert(0,(N-2-i if h[Mr[0]]<h[N-2-i] else Mr[0]))
for i in range(1,N-1): ans.append(max( 0, min(h[Ml[i]],h[Mr[i]])-h[i] ))

print(Ml, Mr, Ans)

#####################################

print(sum(ans))
gshs = Robot(beepers=sum(ans))
moveTop(gshs)
right(gshs)

for num in ans:
    gshs.move()
    moveBottom(gshs)
    moveTop(gshs, num)
    right(gshs)

####################################