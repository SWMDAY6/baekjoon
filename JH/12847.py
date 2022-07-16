n, m = map(int, input().split())
t = list(map(int, input().split()))

sum = 0
for i in range(m):
    sum += t[i]

result = sum
for i in range(m, n):
    sum += t[i] - t[i-m]
    result = max(result, sum)

print(result)

