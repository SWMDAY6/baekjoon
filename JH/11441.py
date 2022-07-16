import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())
sum = [0, A[0]]
for i in range(1, N):
    sum.append(sum[i] + A[i])
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])


"""
## 시간 초과
for _ in range(M):
    i, j = map(int, input().split())
    sum = 0
    for k in range(i-1, j):
        sum += A[k]
    print(sum)
"""
