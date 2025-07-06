import sys
input = sys.stdin.readline

def dfs(idx):
    global count
    if ls[idx] == []:
        count += 1
    visit[idx] = 1
    for x in ls[idx]:
        if not visit[x]:
            dfs(x)

n = int(input())
ls = [[] for _ in range(n)]
val = list(map(int, input().split()))
visit = [0 for _ in range(n)]
start_node = -1
for  i in range(n):
    if val[i] != -1:
        ls[val[i]].append(i)
    else:
        start_node = i

remove_node = int(input())
if remove_node != start_node:
    ls[val[remove_node]].remove(remove_node)
    ls[remove_node] = []
    count = 0
    dfs(start_node)
    print(count)
else:
    print(0)