from collections import deque

n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

possible = False


def bfs():
    teacher_queue = deque()
    visited = [[False]*n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'T':
                teacher_queue.append((i, j))

    while teacher_queue:
        x, y = teacher_queue.popleft()
        for i in range(4):
            tmp_x, tmp_y = x, y
            while True:
                nx = tmp_x + dx[i]
                ny = tmp_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 'X' and visited[nx][ny] == False:
                        visited[nx][ny] = True
                    elif arr[nx][ny] == 'S':
                        return False
                    elif arr[nx][ny] == 'O':
                        break
                    tmp_x, tmp_y = nx, ny
                else:
                    break
    return True


def wall(idx):
    global possible
    if idx == 3:
        if bfs():
            possible = True
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                wall(idx+1)
                arr[i][j] = 'X'


wall(0)
if possible:
    print('YES')
else:
    print('NO')
