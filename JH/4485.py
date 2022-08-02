# 녹색 옷 입은 애가 젤다지?
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))
    dist[0][0] = 0

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                ncost = cost + graph[nx][ny]

                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(queue, (ncost, nx, ny))


cnt = 1

while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]

    dijkstra()
    cnt += 1
