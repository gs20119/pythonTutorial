
from cs1robots import *
load_world('p3.wld')
reader = Robot()

def left(robot):
    robot.turn_left()

def right(robot):
    for _ in range(3): left(robot)

def around(robot):
    for _ in range(2): left(robot)

#######################################################

def moveTop(robot, xxMAP):
    while not robot.facing_north(): left(robot)
    xMAP = []
    for val in xxMAP:
        xMAP.append(val+1 if robot.on_beeper() else 0)
        if robot.front_is_clear(): robot.move()
    return xMAP

def moveBottom(robot):
    while not robot.facing_north(): left(robot)
    around(robot)
    while robot.front_is_clear(): robot.move()

#######################################################

temp = [0]
while not reader.facing_north(): left(reader)
while reader.front_is_clear():
    reader.move()
    temp.append(0)
moveBottom(reader)

MAP = [moveTop(reader,temp)]
right(reader)
reader.move()
moveBottom(reader)

while True:
    MAP.append(moveTop(reader,MAP[-1]))
    right(reader)
    if not reader.front_is_clear(): break
    reader.move()
    moveBottom(reader)

print(MAP)

######################################################

def largeRecHist(H:list) -> int:
    H.append(-1)
    stack = []
    stack.append(-1)
    ans = (0, 0, 0, 0)
    for right in range(len(H)):
        while len(stack) > 1 and H[right] < H[stack[-1]]:
            ceil = stack[-1]
            stack.pop()
            left = stack[-1]
            area = (right-left-1)*H[ceil]
            if ans[2] < area:
                ans = (H[ceil], right-left-1, area, right)
        stack.append(right)
    return ans

xAns, yAns = 0, 0
wAns, hAns = 0, 0
MAX = 0
for x, xMAP in enumerate(MAP):
    width, height, area, y = largeRecHist(xMAP)
    if area > MAX:
        wAns, hAns = width, height
        xAns, yAns, MAX = x, y, area

print(xAns, yAns, wAns, hAns, MAX)

####################################################

gshs = Robot()
for i in range(xAns): gshs.move()
left(gshs)
for i in range(yAns-1): gshs.move()

gshs.set_trace('blue')
left(gshs)
for i in range(wAns-1): gshs.move()
left(gshs)
for i in range(hAns-1): gshs.move()
left(gshs)
for i in range(wAns-1): gshs.move()
left(gshs)
for i in range(hAns-1): gshs.move()