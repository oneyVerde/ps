from collections import deque

def bfs(r, c):
    flag = 0
    ans = 0
    if visit[r][c] == False:
        q = deque([(r,c,0)])
    visit[r][c] = True
    while q:
        if flag == 1:
            break
        r, c, cnt = q.popleft()
        for i in range(8):
            row = r + dx[i]
            col = c + dy[i]
            if 0 <= row < n and 0 <= col < m and visit[row][col] == False:
                if graph[row][col] == 1:
                        ans = cnt+1
                        flag = 1
                        break
                else:
                    visit[row][col] = True
                    q.append((row,col,cnt+1))
    return ans

def init(v):
    for i in range(n):
        for j in range(m):
            visit[i][j] = False

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
maxi = 0


dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

for i in range(n):
    for j in range(m):
        visit = [[False for _ in range(m)] for _ in range(n)]
        if graph[i][j] == 0:
            maxi = max(maxi, bfs(i,j))

print(maxi)