n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(2)]

# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우
dp[0][0] = arr[0]
dp[1][0] = -1e9

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+ arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

print(max(max(dp[0]), max(dp[1])))
