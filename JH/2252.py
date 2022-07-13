### 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]

queue = deque()
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    v = queue.popleft()
    result.append(v)
    for i in graph[v]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

print(*result)
