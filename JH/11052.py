n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i-k]+p[k-1], dp[i])

print(dp[n])