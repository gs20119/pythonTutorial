
import turtle
from random import randint

bugs = [ turtle.Turtle() for i in range(50) ]
win = turtle.Screen()
win.bgcolor("black")
win.setup(1000, 1000)

turtle.colormode(255)
turtle.tracer(10)

for bug in bugs:
    bug.color(100+randint(1,100), 100+randint(1,100), 100+randint(1,100))

def turnRandom(bug):
    bug.setheading(90*randint(0,3))

def simulate(bugs, screen):
    for bug in bugs: turnRandom(bug)
    for bug in bugs: bug.forward(10)

def end(x,y):
    turtle.bye()
win.onclick(end)

for i in range(10000):
    win.ontimer(simulate(bugs, win), 250)
    win.update()

