def dfs(start, dest, cnt):
    go = []
    for x in route[start]:
        if x == dest:
            return cnt
        if len((h[x])) == 1 and x not in vis:
            vis.append(x)
        else:
            if x not in vis:
                vis.append(x)
                go.append(x)
    for x in go:
        return dfs(x, dest, cnt+1)


n = int(input())
vis = [0]
h = {}
route = {}
for x in range(1, n+1):
    l = list(map(int, input().split()))
    for y in l[1:]:
        if h.get(y):
            h[y].extend([x])
        else:
            h[y] = list()
            h[y].extend([x])
        if route.get(y):
            route[y].extend(l[1:])
        else:
            route[y] = l[1:]
dest = int(input())
result = dfs(0, dest, 0)
if result == None:
    print(-1)
else:
    print(result)

"""
오류코드...
import sys
from queue import PriorityQueue
input = sys.stdin.readline


def bfs():
    queue = PriorityQueue()
    visited_station = []    # 역의 번호가 다양하기때문에 배열X
    visited_line = []  # 방문한 호선
    result = 0

    queue.put(0)
    visited_station.append(0)

    while queue:
        v = queue.get()
        line = []  # 여러 호선이 있을 수 있음

        # 호선 찾기
        for i in range(n):
            for x in subway[i+1]:
                if x == v:
                    line.append(i+1)

        for li in line:
            if li not in visited_line:
                for station in subway[li]:
                    if station == dest:
                        print(result)
                        return
                    if station not in visited_station:
                        queue.put(station)
                        visited_station.append(station)
                visited_line.append(li)
                result += 1
    print(-1)
    return


n = int(input().strip())
subway = [-1]
for i in range(n):
    input_list = list(map(int, input().split()))
    subway.append(input_list[1:])

dest = int(input().strip())

bfs()
"""
