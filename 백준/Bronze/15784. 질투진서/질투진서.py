N, a, b = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]
n = ls[a-1][b-1]
res = "HAPPY"

if ( n < max([ls[i][b-1] for i in range(N)]) ) or ( n < max([ls[a-1][j] for j in range(N)]) ):
    res = "ANGRY"

print(res)