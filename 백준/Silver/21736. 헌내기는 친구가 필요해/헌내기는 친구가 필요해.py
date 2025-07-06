from collections import deque

def dfs(x,y):
    global count, ls, visit
    queue = deque([(x,y)])
    visit[x][y] = 1
    while queue:
        curr_x, curr_y = queue.popleft()
        for i in range(4):
            xx = curr_x + dir[i][0]
            yy = curr_y + dir[i][1]
            if 0 <= xx < n and 0 <= yy < m:
                if ls[xx][yy] != 'X' and visit[xx][yy] == 0:
                    if ls[xx][yy] == 'P':
                        count += 1
                    visit[xx][yy] = 1
                    queue.append((xx,yy))

n, m = map(int, input().split())
ls = []
count = 0
dir = [[1,0], [0,1], [-1,0], [0,-1]]
curr = (0,0)
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    s = str(input())
    tmp = []
    for j in range(m):
        if s[j] == 'I':
            curr = (i,j)
        tmp.append(s[j])
    ls.append(tmp)

dfs(curr[0], curr[1])

if count == 0:
    print('TT')
else:
    print(count)