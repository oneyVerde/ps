n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

path = [[0]*n for _ in range(n)]
path[n-1][n-1] = 1
board[n-1][n-1] = 1

for i in range(2*(n-1), -1, -1):
    for j in range(min(n-1, i), max(0, i-n+1)-1, -1):
        row, col = j+board[j][i-j], i-j+board[j][i-j]
        if 0 <= row < n and 0 <= col < n:
            path[j][i-j] = path[row][i-j] + path[j][col]
        else:
            if 0 <= row < n:
                path[j][i-j] += path[row][i-j]
            if 0 <= col < n:
                path[j][i-j] += path[j][col]


print(path[0][0])