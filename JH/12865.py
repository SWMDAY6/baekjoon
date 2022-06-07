n, k = map(int, input().split())
arr = []

for _ in range(n):
    w, v = map(int,input().split())
    arr.append([w,v])

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w]+v)

print(dp[n][k])    
