import sys
from collections import deque
d = deque()
size = 0
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    ls = list(map(str, input().split()))
    if ls[0] == 'push':
        d.append(ls[1])
        size += 1
    elif ls[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(d.popleft())
            size -= 1
    elif ls[0] == 'size':
        print(size)
    elif ls[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif ls[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(d[0])
    else:
        if size == 0:
            print(-1)
        else:
            print(d[-1])