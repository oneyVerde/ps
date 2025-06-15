from collections import deque

def bfs(row, col):
    visit[row][col] = 1
    queue = deque()
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            rr = r + direction[i][0]
            cc = c + direction[i][1]
            if 0 <= rr < n and 0 <= cc < n:
                if visit[rr][cc] == 0:
                    queue.append((rr,cc))
                    visit[rr][cc] = visit[r][c] + 1
    return visit[end_row][end_col]-1


direction = [[-2,-1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]] # x,y
t = int(input())
for _ in range(t):
    n = int(input())
    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())
    visit = [[0 for _ in range(n)] for _ in range(n)]
    print(bfs(start_row, start_col))
