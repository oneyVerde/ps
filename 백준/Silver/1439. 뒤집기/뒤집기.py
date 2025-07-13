import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))
count = [0, 0]
before = -1
for i in s:
    if before == -1:
        count[i] += 1
    if before != -1 and before != i:
        count[i] += 1
    before = i
print(min(count))