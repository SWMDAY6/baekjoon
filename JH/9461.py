t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
dp = [1,1,1,2,2]

for i in range(5, max(arr)):
    dp.append(dp[i-1] + dp[i-5])

for i in arr:
    print(dp[i-1])
