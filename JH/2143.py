import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())
n = int(input().strip())
arr_a = list(map(int, input().split()))
m = int(input().strip())
arr_b = list(map(int, input().split()))

dict_a = defaultdict(int)
dict_b = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        dict_a[sum(arr_a[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        dict_b[sum(arr_b[i:j+1])] += 1

result = 0

for key in dict_a.keys():
    result += dict_b[t - key] * dict_a[key]
 
print(result)

