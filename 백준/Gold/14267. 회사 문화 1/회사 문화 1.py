import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    global praise, visit
    visit[idx] = 1

    for node in tree[idx]:
        if not visit[node]:
            praise[node] += praise[idx]
            dfs(node)


num_staff, num_praise = map(int, input().split())
superior = list(map(int, input().split()))

tree = [[] for _ in range(num_staff)] # 인접 리스트
praise = [0 for _ in range(num_staff)]
visit = [0 for _ in range(num_staff)]
for _ in range(num_praise):
    staff, praise_weight = map(int, input().split())
    praise[staff-1] += praise_weight # 한명이 여러번 칭찬 받는 경우도 존재

for i in range(num_staff):
    if superior[i] != -1:
        tree[superior[i]-1].append(i)
for i in range(num_staff):
    if not visit[i]:
        dfs(i)

print(*praise)
