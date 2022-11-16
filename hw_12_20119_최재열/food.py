from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh()

    # TODO 함수 수정
    def refresh(self):
        self.goto(randint(-200,200), randint(-200,200))