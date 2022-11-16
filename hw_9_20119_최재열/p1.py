
from cs1robots import *
load_world('p1.wld')
counter = Robot()
gshs = Robot()
gshs.set_pause(0.1)
N = int(input())

#####################################

def move(robot):
    if not robot.front_is_clear():
        robot.turn_left()
    robot.move()

def count(robot):
    c = 0
    while robot.on_beeper():
        c += 1
        robot.pick_beeper()
    for i in range(c): robot.drop_beeper()
    return c

total = count(counter)
counter.move()
while counter.get_pos() != (1,1):
    total += count(counter)
    move(counter)

#####################################

ans = 0

for i in range(total):
    move(gshs)
    skipped = 0
    while skipped < N or not gshs.on_beeper():
        if gshs.on_beeper():
            skipped += 1
        move(gshs)
        ans += 1
    gshs.pick_beeper()

print(ans)

####################################