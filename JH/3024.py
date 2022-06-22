import sys

n = int(input())

board = []

for i in range(n):
    tmp = list(map(str, sys.stdin.readline().strip()))
    board.append(tmp)

dx = [1,1,1,0]
dy = [-1,0,1,1]

for i in range(n):
    for j in range(n):
        if board[i][j] != '.':
            for k in range(4):
                sw = 0
                for l in range(1,3):
                    if i+dy[k]*l < 0 or i+dy[k]*l>=n or j+dx[k]*l<0 or j+dx[k]*l>=n:
                        sw=1
                        break
                    
                    if board[i+dy[k]*l][j+dx[k]*l] != board[i][j]:
                        sw=1
                        break
                if sw == 0:
                    print(board[i][j])
                    exit(0)

print("ongoing")
exit(0)