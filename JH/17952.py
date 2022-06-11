from collections import deque
import sys

input = sys.stdin.readline

result, score = deque(), deque()
n = int(input())

for i in range(n):
    input_arr = list(map(int, input().split()))
    if input_arr[0] == 1:
        score.append([input_arr[1], input_arr[2]])
    else:
        pass
    if score:
        score[-1][-1] -= 1
        if score[-1][-1] == 0:
            result.append(score[-1][0])
            score.pop()

print(sum(result))