from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
order = deque(map(int, input().split()))
ls = deque(i for i in range(1, n+1))
count = 0

while order:
    length = round(len(ls)//2)
    if order[0] == ls[0]:
        ls.popleft()
        order.popleft()
        continue
    elif ls.index(order[0]) <= length:
        tmp = ls.popleft()
        ls.append(tmp)
        count += 1
    else:
        tmp = ls.pop()
        ls.appendleft(tmp)
        count += 1

print(count)