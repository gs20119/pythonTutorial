
from turtle import *
size = 7 #원판의 갯수
setup(800, 800)
colormode(255)

#########################################################

class Disc:
    def __init__(self, n):
        self.n = n
        self.x, self.y = 0, 0
        self.body = Turtle()
        self.body.shape('square')
        self.body.shapesize(stretch_wid=1, stretch_len=n)
        self.body.color( 100+int(150/size)*n, 100, 100+int(150/size)*(size-n) )
        self.body.penup()
        self.body.speed('normal')

    def move(self, x_, y_):
        self.body.goto(x_,self.y)
        self.body.goto(x_, y_)
        self.x, self.y = x_, y_

#########################################################

class Tower(list):
    def __init__(self, x):
        super().__init__()
        self.x = x

    def append(self, d):
        super().append(d)
        d.move(self.x, -80+20*len(self))

    def pop(self):
        d = super().pop()
        d.move(d.x, 150)
        return d

#########################################################

def hanoi(n, a, b, c): # want a -> c
    if n > 0:
        hanoi(n-1, a, c, b)
        c.append(a.pop())
        hanoi(n-1, b, a, c)

#########################################################

def main():
    t1 = Tower(-200) #타워의 위치 3, 5, 7
    t2 = Tower(0)
    t3 = Tower(200)
    for i in range(size, 0, -1):
        t1.append(Disc(i))
    hanoi(size, t1, t2, t3)
    exitonclick()

onkey(main, "space")
listen()
mainloop()

#########################################################