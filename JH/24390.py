m, s = map(int, input().split(':'))

count = 1  # 조리시작 버튼

count += (m//10 + m % 10)
if s < 30:
    count += (s//10)
elif s >= 30:
    count += ((s-30)//10)

print(count)

'''
분/초 추가 선택하고 조리시작 버튼을 누르면 -1 번 되는 걸 감안 해야함!
'''
