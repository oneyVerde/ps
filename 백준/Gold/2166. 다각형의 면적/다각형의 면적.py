n = int(input())
ls = []
for _ in range(n):
    ls.append(tuple(map(int, input().split())))

ans = 0
for i in range(1, n-1):
    x1, y1 = ls[0][0], ls[0][1]
    x2, y2 = ls[i][0], ls[i][1]
    x3, y3 = ls[i+1][0], ls[i+1][1]

    ans += (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)/2

print(abs(ans))