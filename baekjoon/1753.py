import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    global distance
    queue = [] # 우선순위 큐
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    while queue:
        dist, node = heapq.heappop(queue) # 거리가 먼저 비교 되도록
        if distance[node] != dist:
            continue
        for v, w in graph[node]:
            cand = dist + w
            # 갱신
            if cand < distance[v]:
                distance[v] = cand
                heapq.heappush(queue, (cand, v))

INF = 1e9
V,E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])