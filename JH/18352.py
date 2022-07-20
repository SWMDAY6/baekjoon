# 특정 거리의 도시 찾기
from dis import dis
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
visited = [False] * (n+1)

queue = deque([x])
while queue:
    now = queue.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

if k in distance:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)
