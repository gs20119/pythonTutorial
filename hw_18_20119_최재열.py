
from tkinter import *
import random
import time

app = Tk()
app.title("Bouncing Ball")

canvas = Canvas(app, width=500, height=500)
canvas.pack()
canvas.update()


class Mover:
    def __init__(self, x_, v_, a_):
        self.x, self.v, self.a = x_, v_, a_
        self.left = -3000
        self.right = 3000

    def setlim(self, l_, r_):
        self.left = l_
        self.right = r_

    def update(self, dt):
        self.v += self.a*dt
        self.x += self.v*dt
        if self.x<self.left:
            self.v *= -0.95
            self.x = self.left
        elif self.x>self.right:
            self.v *= -0.95
            self.x = self.right

    def value(self):
        return self.x

def randomColor():
    de =("%02x"%random.randint(0,255))
    re = ("%02x"%random.randint(0,255))
    we = ("%02x"%random.randint(0,255))
    ge = "#"
    return ge+de+re+we

class Ball:
    def __init__(self):
        self.x = Mover(250, random.randint(-30,30), 0)
        self.y = Mover(200, random.randint(-40,20), 5)
        self.x.setlim(0,450)
        self.y.setlim(0,450)
        self.body = canvas.create_oval(240, 260, 190, 210, fill=randomColor())

    def update(self):
        self.x.update(0.1)
        self.y.update(0.1)

    def draw(self):
        X = self.x.value()
        Y = self.y.value()
        canvas.moveto(self.body, X, Y)



balls = [Ball() for i in range(8)]
while True:
    for ball in balls :
        ball.update()
        ball.draw()
    app.update()
    time.sleep(0.01)

app.mainloop()
sys.exit()