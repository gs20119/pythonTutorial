import turtle
import sys

################################################################################
# 사용자 입력변수
################################################################################

## 윈도우의 창제목
TITLE="파이썬 거북이로 별그리기"

## 그리기를 시작하는 X좌표
START_X=-100

## 그리기를 시작하는 Y좌표
START_Y=100

## 거북이 색상 (결국 이 리스트의 숫자가 거북이 숫자) - 이 리스트가 1이면 거북이가 1개^^
TURTLE_COLORS=['blue', 'red', 'green', 'purple', 'gray']

## 거북이가 앞으로 이동하는 거리 (결국 별모양의 한변 길이)
TURTLE_FORWORD=200

## 거북이 몇번에 걸쳐 앞으로 가는지 (1이면 한번에 바로)
TURTLE_FORWORD_TIMES=10;

## 거북이 별꼭지점에서 몇번에 걸쳐 방향을 트는지 (1이면 한번에 바로)
TURTLE_TURN_TIMES=2;

################################################################################
# 사용자 입력변수 체크
################################################################################

if TITLE == '' :
    print("TITLE 이 없습니다.")
    sys.exit(0)

if START_X<-300 or START_X>300:
    print("START_X는 -300과 300사이입니다.")
    sys.exit(0)

if START_Y<-300 or START_Y>300:
    print("START_Y는 -300과 300사이입니다.")
    sys.exit(0)

if len(TURTLE_COLORS)<1 :
    print("TURTLE_COLORS에는 1개이상의 색이 있어야 합니다.")
    sys.exit(0)

def setup_turtle(a_turtle, x, y) :

    if len(TURTLE_COLORS)==0 : return

    ## 거북이를 들어서 시작지점에서 화면에서 그리지 않도록 한다.
    a_turtle.penup()

    # 거북이의 좌표를 설정한다.
    a_turtle.setposition(x, y)

    ## 펜을 내려놓는다.
    a_turtle.pendown()

    ## 첫번째 거북이 색을 가져온다
    c = TURTLE_COLORS.pop(0)

    # 색을 정한다.
    a_turtle.color(c, c)

def move_turtles(turtles) :

    while True :

        for _ in range(TURTLE_FORWORD_TIMES):
            for a_turtle in turtles:
                a_turtle.forward(TURTLE_FORWORD/TURTLE_FORWORD_TIMES)

        for a_turtle in turtles:
            a_turtle.left(360*2/5)

        ## 새로운 거북이를 만들자.
        if len(TURTLE_COLORS)>0 :
            new_turtle=turtle.Turtle()
            setup_turtle(new_turtle, START_X, START_Y)
            turtles.append(new_turtle)

################################################################################
# 메인함수 (main)
################################################################################

## 창제목을 설정한다
turtle.title(TITLE)

## 거북이 리스트를 만든다
turtles = list()

turtle1=turtle.Turtle()
setup_turtle(turtle1, START_X, START_Y)
turtles.append(turtle1)
move_turtles(turtles)