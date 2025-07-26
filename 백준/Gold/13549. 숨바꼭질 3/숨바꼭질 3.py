import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [100000 for _ in range(200001)]

for i in range(n+1):
    dp[i] = n-i
    dp[2*i] = n-i

for i in range(n+1, m+1):
    if i%2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i+1] + 1, dp[i//2])
    if i%2 == 1:
        dp[i] = min(dp[i-1] + 1, dp[i+1] + 1)
    dp[2*i] = min(dp[2*i], dp[i])

print(dp[m])