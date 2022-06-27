import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(2)] for _ in range(n)]

dp[0][1] = arr[0][2]
if n >= 2:
    dp[1][0] = arr[0][2]
    dp[1][1] = arr[1][2]

for i in range(2, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
    dp[i][1] = dp[i-1][0] + arr[i][2]

print(max(dp[n-1][0], dp[n-1][1]))