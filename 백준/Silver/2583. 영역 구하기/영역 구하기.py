from sys import*
setrecursionlimit(10**6)

def dfs(x,y):
    global count
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if graph[x][y] == 1:
        return 0
    
    graph[x][y] = 1
    count += 1

    for i in range(4):
        xx = x + dir[i][0]
        yy = y + dir[i][1]
        dfs(xx, yy)

    return count


n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
dir = [[0,-1],[0,1],[-1,0],[1,0]]
count = 0
total = []

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, input().split())
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            graph[i][j] = 1

for i in range(n):
    for j in range(m):
        res = dfs(i,j)
        if res > 0:
            total.append(res)
        count = 0

total.sort()
print(len(total))
for i in total:
    print(i, end=' ')