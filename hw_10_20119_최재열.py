
import turtle

gshs = turtle.Turtle()
win = turtle.Screen()

def drawTree(robot, gen, theta):
    if gen == 0: return
    robot.forward(gen*15)
    robot.left(theta)
    drawTree(robot, gen-1, theta)
    robot.right(2*theta)
    drawTree(robot, gen-1, theta)
    robot.left(theta)
    robot.backward(gen*15)

gshs.sety(-105)
gshs.left(90)
drawTree(gshs,7,20)
win.exitonclick()