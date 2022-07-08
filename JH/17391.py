import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global arr, n, m
    queue = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [1, 0]
    dy = [0, 1]

    visited[0][0] = 1
    queue.append((0,0,0))

    while queue:
        x, y, w = queue.popleft()
        if x == (n-1) and y == (m-1):
            return w
        
        for i in range(2):
            for j in range(1, arr[x][y]+1):
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if (0 <= nx < n and 0 <= ny < m) and (visited[nx][ny] == 0):
                    queue.append((nx,ny, w+1))
                    visited[nx][ny] = 1

arr = []

n, m = map(int, input().split())

for _ in range(n):
    arr.append(list(map(int, input().split())))

print(bfs())