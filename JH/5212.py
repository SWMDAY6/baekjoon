import sys
import copy

def Sea_Check(x,y,arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            count += 1
            continue
        elif arr[nx][ny] == '.':
            count += 1

    return count

r, c = map(int, input().split())

arr= []
for i in range(r):
    arr.append(list(map(str, sys.stdin.readline().strip())))

copy_arr = copy.deepcopy(arr)

for i in range(r):
    for j in range(c):
        if arr[i][j] == "X":
            if Sea_Check(i,j,arr) >= 3:
                copy_arr[i][j] = '.'

start_row = 0
start_col = 0
end_row = 0
end_col = 0
min_index = c-1
max_index = 0

for i in range(r):
    if 'X' in copy_arr[i]:
        start_row = i
        break

for i in range(r-1, -1, -1):
    if 'X' in copy_arr[i]:
        end_row = i
        break

for i in range(start_row,  end_row+1):
    tmp = [i for i, value in enumerate(copy_arr[i]) if value == 'X']
    if not tmp:
        continue
    min_tmp = tmp[0]
    max_tmp = tmp[-1]
    min_index = min(min_index, min_tmp)
    max_index = max(max_index, max_tmp)

for i in range(start_row, end_row+1):
    for j in range(min_index, max_index+1):
        print(copy_arr[i][j], end='')
    print()