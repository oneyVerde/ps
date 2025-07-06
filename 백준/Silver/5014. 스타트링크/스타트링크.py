from collections import deque

def bfs(n):
    global flag
    queue = deque()
    visit[n] = 1
    queue.append((n, 0))

    while queue:
        num, count = queue.popleft()
        if num == target:
            flag = 1
            print(count)
            break

        plus = num + up
        if plus <= total:
            if visit[plus] == 0:
                visit[plus] = 1
                queue.append((plus, count+1))

        sub = num - down
        if sub >= 1:
            if visit[sub] == 0:
                visit[sub] = 1
                queue.append((sub,count+1))
                
total, start, target, up, down = map(int, input().split())

visit = [0] * (total+1)
flag = 0

bfs(start)
if flag == 0:
    print("use the stairs")