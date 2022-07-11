import sys
input = sys.stdin.readline

n, m = map(int,input().split())
money = list(int(input()) for _ in range(n))
l, r = min(money), sum(money)

# 이분탐색  
while l <= r:
    mid = (l+r) // 2
    charge = mid
    count = 1   #인출횟수
    for i in range(n):
        if charge < money[i]:
            charge = mid
            count += 1
        charge -= money[i]
    
    if count > m or mid < max(money):
        l = mid + 1
    else:
        r = mid - 1
        k = mid

print(k)