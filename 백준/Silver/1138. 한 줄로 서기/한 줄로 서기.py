n = int(input())
ls = list(map(int, input().split()))

res = [0 for _ in range(n)]
for i, num in enumerate(ls):
    count = 0
    for j, idx in enumerate(res):
        if idx == 0 and count < num:
            count += 1
        elif idx == 0 and count == num:
            res[j] = i+1
            break
print(*res)