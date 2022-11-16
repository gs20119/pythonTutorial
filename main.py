from cs1robots import *

create_world()
gshs = Robot(beepers=10)
gshs.set_trace('blue')

gshs.move()
for i in range(4):
    gshs.turn_left()
    gshs.move()
    gshs.turn_right()
    gshs.move()
    gshs.move()

#gshs.drop_beeper()
#gshs.move()
#gshs.turn_left()
#gshs.move()
#gshs.drop_beeper()
#gshs.pick_beeper()



