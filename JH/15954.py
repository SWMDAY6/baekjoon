import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def distribute(m, arr):
    result = 0
    for i in arr:
        result += (i-m)**2
    return result/len(arr)


result_list = list()

for i in range(n-k+1):
    for j in range(n-k-i+2):
        tmp = arr[i: i + k + j]
        m = sum(tmp) / len(tmp)
        dis = distribute(m, tmp)
        result_list.append(dis)

result = min(result_list)

print(math.sqrt(result))
