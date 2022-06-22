import sys
input = sys.stdin.readline

def dfs(x,y,n):
    global result_white, result_blue

    num_check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(paper[i][j] != num_check):
                for k in range(2):
                    for l in range(2):
                        dfs(x+ k*n//2, y+ l*n//2, n//2)
                return
    if num_check == 0:
        result_white += 1
    else:
        result_blue += 1

n = int(input())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

result_white = 0
result_blue = 0

dfs(0,0,n)
print(f'{result_white}\n{result_blue}')