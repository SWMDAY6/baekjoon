import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    global m, n
    queue = deque()
    cnt = 1
    queue.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 0:
                    cnt += 1
                    graph[ny][nx] = 1
                    queue.append((ny, nx))
    return cnt


m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = 1

res = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))

print(len(res))
print(*sorted(res))
