import sys
input = sys.stdin.readline

t = int(input())
while t:
    t -= 1
    n = int(input())
    ls = []
    for i in range(n):
        ls.append(tuple(map(int, input().split())))

    ls.sort(key=lambda x:x[0])
    count = 0
    current = ls[0][1]
    for v in ls:
        if current >= v[1]:
            count += 1
            current = v[1]
    print(count)