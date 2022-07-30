# 함께 블록 쌓기
n, m, h = map(int, input().split())
dp = [[1]+[0]*h for i in range(n+1)]
for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    blocks = list(map(int, input().split()))
    for x in blocks:
        for j in range(x, h+1):
            dp[i][j] += dp[i-1][j-x]
print(dp[n][h] % 10007)
