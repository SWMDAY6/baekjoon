import sys
import heapq as hq
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
time = 0
heap = []
result = 0

for i in range(m):
    hq.heappush(heap, [-b[i], a[i]])
n *= 24
while n > time and heap:
    y, x = hq.heappop(heap)
    if (100-x) // (-y) < n-time:
        tmp = x + (-y * ((100-x) // (-y)))
        if tmp == 100:
            result += 100
        else:
            hq.heappush(heap, [-(100-tmp), tmp])
        time += (100-x)//(-y)
    else:
        result += x + (n-time)*(-y)
        time += (n-time)

for y, x in heap:
    result += x
print(result)
