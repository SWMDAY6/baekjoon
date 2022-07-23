# 최대공약수 구하기
def gcd(a, b):
    while(b):
        tmp = a % b
        a = b
        b = tmp
    return a


max, min = map(int, input().split())
div = min // max
a, b = 1, div

for i in range(1, div//2+1):
    if div % i == 0:
        c = i
        d = div//i
        if gcd(c, d) != 1:
            continue
        if a+b > c+d:
            a = c
            b = d

print(a*max, b*max)

'''
** python에서 제공하는 math 라이브러리
from math import gcd

print(gcd(x,y))
'''
