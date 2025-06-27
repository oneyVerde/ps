import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(1, n+2)]
sq = [i**2 for i in range(1, 317)]

for i in range(1, n+1):
    tmp = []
    for j in sq:
        if i < j:
            break
        tmp.append(dp[i-j])

    dp[i] = min(tmp) + 1

print(dp[n])