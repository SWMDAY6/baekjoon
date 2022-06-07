import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    k = int(input())
    file_arr = list(map(int, input().split()))
    
    dp = [[0]*k for _ in range(k) ]
    for i in range(k-1):
        dp[i][i+1] = file_arr[i] + file_arr[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + file_arr[j]

    for d in range(2, k): #부분 파일의 길이
        for i in range(k-d):
            j = i+d
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i, j)]
            dp[i][j] += min(minimum)

    print(dp[0][k-1])

