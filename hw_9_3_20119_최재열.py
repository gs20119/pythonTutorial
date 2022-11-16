
from cs1robots import *
import cs1robots
create_world()
gshs = Robot(avenue=1, street=10, beepers=10000)
size = 6 #원판의 갯수

#########################################################

class Disc:
    def __init__(self, n):
        # TODO: instance 변수 n(size), x, y(piles) 추가
        self.n = n
        self.x, self.y = 0, 0

#########################################################

class Tower(list):
    def __init__(self, x):
        # TODO: instance 변수 x(stick) 추가
        self.x = x

    # TODO: push 함수 구현(d는 Disc)
    def push(self, d):
        # TODO: 넘어온 d의 정보를 갱신시킬 것.
        gshs._x = d.x = self.x
        gshs._y = d.y = len(self)+1
        super().append(d)
        for _ in range(d.n):
            cs1robots._world.add_beeper(gshs._x, gshs._y)
        pause(0.1)
        gshs._refresh()

    def pop(self):
        # TODO: 상속한 List의 함수 pop 오버라이딩
        d = super().pop()
        gshs._x = d.x
        gshs._y = d.y
        for i in range(d.n):
            gshs.pick_beeper()
        pause(0.1)
        return d;

#########################################################

def hanoi(n, a, b, c): # want a -> c
    # TODO :하노이 함수 작성
    if n > 0:
        hanoi(n-1, a, c, b)
        pause(0.1)
        c.push(a.pop())
        pause(0.1)
        hanoi(n-1, b, a, c)
        pause(0.1)

#########################################################

def main():
    t1 = Tower(3) #타워의 위치 3, 5, 7
    t2 = Tower(5)
    t3 = Tower(7)
    for i in range(size, 0, -1):
        #TODO: 첫 번째 타워에 디스크 넣기
        t1.push(Disc(i))
    hanoi(size, t1, t2, t3)

if __name__ == "__main__":
    main()

#########################################################