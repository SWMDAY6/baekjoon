import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (visited[nx][ny] == False) and arr[nx][ny] >= t:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n, m = map(int, input().split())
arr = []

for i in range(n):  # 총 입력배열 행 수
    input_tmp = list(map(int, input().split()))
    tmp = []
    for k in range(m):
        tmp.append(sum(input_tmp[3*k:3*(k+1)]))

    arr.append(tmp)

t = int(input().strip())
t = 3*t

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] >= t and visited[i][j] == False:
            bfs(i, j)
            cnt += 1

print(cnt)
