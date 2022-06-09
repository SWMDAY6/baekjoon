n = int(input())

child = []
dp = [0 for _ in range(n)]

for i in range(n):
    child.append(int(input()))
    for j in range(i):
        if child[j] < child[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1

print(n - max(dp))
