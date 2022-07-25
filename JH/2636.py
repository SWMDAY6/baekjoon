from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    result.append(cnt)
    return cnt


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = []

time = 0
while True:
    time += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(time-1)
print(result[-2])
