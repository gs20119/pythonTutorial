
import random
with open('gshs.txt', 'w') as f:
    for i in range(10):
        a = random.randint(1,100)
        b = random.randint(1,100)
        c = a+b
        print(a, b, c, file=f)

print(*[1,3,5,7,9], end=' ')