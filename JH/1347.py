import sys

input = sys.stdin.readline

n = int(input())
move = list(str(input()))

# 남 서 북 동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

temp = [[0,0]] #시작 위치

state = 0
 
i, j = 0, 0

for q in move:
 
    if q == 'F':
        i += dx[state % 4]
        j += dy[state % 4]
        temp.append([i,j])
 
    elif q == 'R':
        state += 1
 
    else:
        state += 3
 
x = []
y = []
 
for tmp in temp:
    x.append(tmp[0])
    y.append(tmp[1])
 
x_len = len(set(x))
y_len = len(set(y))
 
x_min = min(x)
 
if x_min < 0:
    x_c = abs(x_min)
else:
    x_c = 0
 
y_min = min(y)
if y_min < 0:
    y_c = abs(y_min)
else:
    y_c = 0
 
visited = [[0] * y_len for _ in range(x_len)]
 
for e in temp:
    visited[e[0]+x_c][e[1]+y_c] = '.'
 
for i in range(x_len):
    if i != 0:
        print()
    for j in range(y_len):
        if visited[i][j] == 0:
            print('#',end='')
        else:
            print(visited[i][j],end='')
