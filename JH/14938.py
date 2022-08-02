# 서강그라운드
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(idx):
    global result
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, idx))
    distance[idx] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for c, i in graph[now]:
            cost = dist + i
            if cost < distance[c]:
                distance[c] = cost
                heapq.heappush(q, (cost, c))
    temp = 0
    for i, d in enumerate(distance):
        if d <= m:
            temp += items[i]
    if temp > result:
        result = temp


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

result = 0

for i in range(n):
    dijkstra(i+1)

print(result)
