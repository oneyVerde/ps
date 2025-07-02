import sys
input = sys.stdin.readline

def binary_search(start, end, target):
    while start <= end:
        middle = (start + end) // 2
        if level[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return name[end+1]


n, m = map(int, input().split())
name, level = [], []
for _ in range(n):
    name_value, level_value = input().split()
    name.append(name_value)
    level.append(int(level_value))

for i in range(m):
    target_value = int(input())
    result = binary_search(0, len(level) - 1, target_value)
    print(result)
