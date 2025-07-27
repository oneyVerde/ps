import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
ls = []
for i in range(m):
    ls.append(tuple(map(int, input().split())))

ls.sort(key=lambda x:x[0])
bf = ls[0]
ls.sort(key=lambda x:x[1])
pf = ls[0]
print(min(math.ceil(n/6) * bf[0], n//6 * bf[0] + n%6 * pf[1], n*pf[1]))