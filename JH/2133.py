n = int(input())
dp = [0] * (n+1)

if n % 2 != 0:
    print(0)
else:
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2
    print(dp[n])

### 다시 풀기
# n == 1 일때, dp[2] 에 값을 넣으면 인덱스 에러남!!
'''
n = int(input())
dp = [0] * (n+1)
dp[2] = 3 ### 오류 코드 (if문으로 n==1일때 따로 해줘야함)

for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 +2
    else:
        dp[i] = 0

print(dp[n])
'''