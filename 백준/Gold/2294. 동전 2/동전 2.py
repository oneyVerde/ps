n,k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [10001 for _ in range(k+1)]
dp[0] = 0
for i in range(1, k+1):
    for j in coin:
        if i >= j:
            dp[i] = min(dp[i], dp[i-j]+1)
print(-1 if dp[k]==10001 else dp[k])