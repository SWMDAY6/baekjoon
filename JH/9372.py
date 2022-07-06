import sys

def dfs(v, count):
    visited[v] = 1

    for i in plain[v]:
        if visited[i] == 0:
            count = dfs(i, count+1)
    
    return count

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    plain = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        plain[a].append(b)
        plain[b].append(a)
    
    visited = [0] * (n+1)

    result = dfs(1, 0)
    print(result)




