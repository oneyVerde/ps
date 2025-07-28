import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
fix = [False for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
rev_distance = [INF for _ in range(n+1)]
distance[0], rev_distance[0] = 0, 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    rev_graph[b].append((a,c))

    if a == start:
        distance[b] = c

    if b == start:
        rev_distance[a] = c

def dijkstra(st, distance, graph):
    distance[st] = 0
    while 1:
        idx = ""
        for i in range(1, n+1):
            if fix[i]:
                continue
            if idx == "":
                idx = i
            elif distance[i] < distance[idx]:
                idx = i
        if idx == "":
            break
        fix[idx] = True
        for v in graph[idx]:
            distance[v[0]] = min(distance[v[0]], distance[idx] + v[1])

    return distance

distance = dijkstra(start, distance, graph)


fix = [False for _ in range(n+1)]

rev_distance = dijkstra(start, rev_distance, rev_graph)

for i in range(1, n+1):
    distance[i] += rev_distance[i]

print(max(distance))