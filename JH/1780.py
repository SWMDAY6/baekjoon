import sys
input = sys.stdin.readline

def dfs(x, y, n):
    global result_minus, result_zero, result_plus
    
    num_check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(paper[i][j] != num_check):
                for k in range(3):
                    for l in range(3):
                        dfs(x+ k*n//3, y+ l*n //3, n//3)
                return
    if num_check == -1:
        result_minus += 1
    elif num_check == 0:
        result_zero += 1
    else:
        result_plus += 1


n = int(input())
paper = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    paper.append(tmp)

result_minus = 0
result_zero = 0
result_plus = 0

dfs(0, 0, n)
print(f'{result_minus}\n{result_zero}\n{result_plus}')