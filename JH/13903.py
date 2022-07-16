import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global dx, dy
    queue = deque()
    for j in range(c):
        if block[0][j] == 1:
            if r == 1:
                return 0
            block[0][j] = 0
            queue.append((0, j))
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for k in range(n):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c and block[nx][ny] == 1:
                    if nx == r-1:
                        return cnt
                    block[nx][ny] = 0
                    queue.append((nx, ny))
    return -1


r, c = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(r)]

n = int(input().strip())

dx = []
dy = []

for _ in range(n):
    x, y = map(int, input().split())
    dx.append(x)
    dy.append(y)

print(bfs())
