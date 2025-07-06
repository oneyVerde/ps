import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx, weight):
    global dp, visit
    visit[idx] = 1

    for node in tree[idx]:
        if not visit[node]:
            dp[node] += dp[idx]
            dfs(node, dp[node])


num_staff, num_praise = map(int, input().split())
superior = list(map(int, input().split()))

tree = [[] for _ in range(num_staff)]
dp = [0 for _ in range(num_staff)]
visit = [0 for _ in range(num_staff)]
has_init = [0 for _ in range(num_staff)]
for _ in range(num_praise):
    staff, praise_weight = map(int, input().split())
    dp[staff-1] += praise_weight
    has_init[staff-1] = 1

for i in range(num_staff):
    if superior[i] != -1:
        tree[superior[i]-1].append(i)
for i in range(num_staff):
    if not visit[i]:
        dfs(i, dp[i])

print(*dp)