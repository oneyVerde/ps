n = int(input())
table = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    m = list(map(int, input().split()))
    table.append(m)

for i in range(n-1, -1, -1):
    if i + table[i][0] <= n:
        dp[i] = max(dp[i+1], dp[i + table[i][0]] + table[i][1])
    else:
        dp[i] = dp[i+1]
print(dp[0])