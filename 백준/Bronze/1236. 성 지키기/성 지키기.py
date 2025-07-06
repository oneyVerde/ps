n,m = map(int, input().split())
row,col = [0]*n,[0]*m
for i in range(n):
    val = str(input())
    for j in range(m):
        if val[j] == 'X':
            row[i] += 1
            col[j] += 1
ans = 0
for i in range(n):
    for j in range(m):
        if row[i] == 0 and col[j] == 0:
            row[i] = 1
            col[j] = 1
            ans += 1
for i in range(n):
    if row[i] == 0:
        ans += 1
for j in range(m):
    if col[j] == 0:
        ans += 1

print(ans)