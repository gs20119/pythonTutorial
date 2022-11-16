
from cs1robots import *
load_world('worlds/frank18.wld')
gshs = Robot(color="light_blue", orientation='E', avenue=1, street=1)  # avenue is x, street is y
gshs.set_trace(color='blue')
gshs2 = Robot(color="green", orientation='E', avenue=1, street=1, beepers=1000)  # avenue is x, street is y
gshs2.set_trace(color='red')

#############################################

face = 0
pos = [1,1]
step = [[1,0],[0,1],[-1,0],[0,-1]]

def counting(robot):
    count = 0
    while robot.on_beeper():
        count += 1
        robot.pick_beeper()
    for i in range(count): robot.drop_beeper()
    return count

def left(robot):
    global face
    robot.turn_left()
    face = (face+1)%4

def right(robot):
    for _ in range(3): left(robot)

############################################

track = []
track.append([face, pos, counting(gshs)])
gshs.move()

for i in range(70):
    pos = [x+i for x,i in zip(pos,step[face])]
    track.append([face, pos, counting(gshs)])
    if pos[0] == 10: left(gshs)
    if pos[0] == 1: right(gshs)
    gshs.move()

track.sort(key=lambda x: x[2], reverse=True)
print(track)

############################################

ans = track[0][1]
for i in range(ans[0]-1): gshs2.move()
gshs2.turn_left()
for j in range(ans[1]-1): gshs2.move()

############################################