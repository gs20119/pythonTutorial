
from cs1robots import *
from math import *
load_world('worlds/foru.wld')
gshs = Robot(beepers=10000)
gshs.set_trace(color='blue')

def drop(robot,n):
    for _ in range(n):
        robot.drop_beeper()

def left(robot):
    robot.turn_left()

def right(robot):
    for _ in range(3): robot.turn_left()

############################################

primes = [2]

def isPrime(x):
    for p in primes:
        if x%p == 0: return False
        if p>sqrt(x): return True
    return True

def nextPrime():
    p = primes[-1]+1
    while not isPrime(p): p += 1
    primes.append(p)
    return p

############################################

drop(gshs,2)
gshs.move()

for i in range(29):
    drop(gshs,nextPrime())
    if gshs.get_pos()[0] == 10: left(gshs)
    if gshs.get_pos()[0] == 1: right(gshs)
    gshs.move()

############################################