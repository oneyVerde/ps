n = int(input())
ls = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i): # 0 <= j < i
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j]+1) # 이전 원소 j가 작을 때만 갱신

print(max(dp))