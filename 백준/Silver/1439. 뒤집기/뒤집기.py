import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))
count = [0, 0]
before = -1
for i in s:
    if before != i:
        count[i] += 1
    before = i
print(min(count))
