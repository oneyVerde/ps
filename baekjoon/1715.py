import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
total = 0
while heap:
    cardA = heapq.heappop(heap)
    if heap:
        cardB = heapq.heappop(heap)
        sum_val = cardA+cardB
        heapq.heappush(heap, sum_val)
        total += sum_val

print(total)