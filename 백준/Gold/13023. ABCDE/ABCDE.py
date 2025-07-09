import sys
input = sys.stdin.readline

def dfs(idx, depth):
    global exist, visit
    visit[idx] = 1
    if depth == 4:
        exist = 1
        return
    for f in friends[idx]:
        if not visit[f]:
            dfs(f, depth+1)
            visit[f] = 0


n, m = map(int, input().split())
friends = [[] for _ in range(n)]
visit = [0 for _ in range(n)]
exist = 0

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    dfs(i, 0)
    visit[i] = 0
    if exist:
        break

print(exist)