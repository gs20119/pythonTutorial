
import numpy as np

def pooling(arr):
    m, n = len(arr), len(arr[0])
    ret = np.zeros((m+2, n+2))
    for i in range(m+2):
        for j in range(n+2):
            ret[i,j] = arr[(i-1)%m, (j-1)%n]
    return ret

def gol_step(arr):
    m, n = len(arr), len(arr[0])
    ker = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    Arr = pooling(arr)
    count = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            count[i,j] = np.sum(ker*Arr[i:i+3, j:j+3])
    A = (arr!=0)*(2<=count)*(count<=3)
    B = (arr==0)*(count==3)
    return np.logical_or(A,B)

current = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]).reshape(4, 4)
next = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]).reshape(4, 4)

print(np.sum(gol_step(current) - next))
