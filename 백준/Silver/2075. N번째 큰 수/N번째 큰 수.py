import heapq
import sys
input = sys.stdin.readline

hq = []
n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    if not hq:
        for i in ls:
            heapq.heappush(hq, i)
    else:
        for i in ls:
            if i > hq[0]:
                heapq.heappush(hq, i)
                heapq.heappop(hq)

print(hq[0])