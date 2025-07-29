n = int(input())
ls = list(map(int, input().split()))
total = [v for v in ls]

for i in range(n):
    for j in range(i):
        if ls[i] > ls[j] and total[i] < total[j] + ls[i]:
            total[i] = total[j] + ls[i]

print(max(total))