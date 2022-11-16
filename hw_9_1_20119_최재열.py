
from random import shuffle
n       = 20
trials  = 1000
dead    = 0
sum     = 0
movement = [(1,0),(0,1),(-1,0),(0,-1)]

###########################################

for t in range(trials):
    a = [[False for i in range(n+2)] for j in range(n+2)]
    x, y = 1+n//2, 1+n//2
    while (1 <= x <= n) and (1 <= y <= n):
        if a[x][y]:
            dead += 1
            break
        a[x][y] = True
        shuffle(movement)
        for i, j in movement:
            if not a[x+i][y+j]:
                x, y = x+i, y+j
                break

###########################################

print(str(100*dead/trials) + '% dead ends')