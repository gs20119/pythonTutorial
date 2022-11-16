
from cs1robots import *
load_world('worlds/ex36.rur.wld')
gshs = Robot()
gshs.set_trace(color='blue')

############################################

x = []
while gshs.front_is_clear():
    gshs.move()
    count = 0
    while gshs.on_beeper():
        gshs.pick_beeper()
        count += 1
    x.append(count)

y = sorted(x)
gshs.turn_left()
gshs.turn_left()

for k in y:
    print(k)
    for i in range(k):
        gshs.drop_beeper()
    gshs.move()

############################################