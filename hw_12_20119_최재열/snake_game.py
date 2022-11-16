import turtle

from score import Score
from turtle import Screen , Turtle, position
import random
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Gshs Snake Game")

#그려지는 과정을 보이지 않고 한 번에 빠르게
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
game_is_on = True
screen.update()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        score_board.refresh_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # TODO snake의 head와 tail과의 충돌 처리 구현

    for segment in snake.snake_body[1:]:
        if snake.head.xcor() == segment.xcor() and snake.head.ycor() == segment.ycor():
            game_is_on = False
            score_board.game_over()
   

#클릭시 종료
screen.exitonclick()