import sys
input = sys.stdin.readline
def solution(x):
    x %= (3600 * 24)
    h = x // 3600
    x %= 3600
    m = x // 60
    x %= 60
    s = x
    
    print(h%24, m, s)

    
h, m, s = map(int, input().split())
q = int(sys.stdin.readline())

sc = h * 3600 + m * 60 + s

for _ in range(q):
    ls = list(map(int, input().split()))
    if ls[0] == 3:
        solution(sc)
    if ls[0] == 1:
        sc += ls[1]
    elif ls[0] == 2:
        sc -= ls[1]
