def go(vn, cnt):
    global visited
    if vn == n:
        return cnt
    if visited[vn]:
        return go(vn+1, cnt)
    result = 0
    for to in fav[vn]:
        if visited[to] == False:
            visited[to] = True
            result = max(result, go(vn+1, cnt+1))
            visited[to] = False
    return max(result, go(vn+1, cnt))


n, m = map(int, input().split())
fav = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())

    if u > v:
        tmp = u
        u = v
        v = tmp
    fav[u].append(v)

result = go(1, 0)
result *= 2
if n > result:
    result += 1

print(result)
