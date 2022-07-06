import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
parent = list(range(v + 1))

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

edges.sort(key=lambda x: x[2])

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

result = 0
for a, b, w in edges:
    if find(a) != find(b):
        union(a, b)
        result += w

print(result)



"""
- 최소 신장 트리
- 가장 적은 비용으로 모든 정점을 연결하는 알고리즘 => 크루스칼, 프림
- 크루스칼 알고리즘 : 간선 정렬을 해야하므로
- 간선이 적으면 크루스칼, 간선이 많으면 프림을 사용한다.

- 위 코드는 크루스칼 알고리즘
"""