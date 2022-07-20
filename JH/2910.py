# 빈도 정렬
n, c = map(int, input().split())
msg = list(map(int, input().split()))
dic = dict()

for x in msg:
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] += 1

sorted_dict = sorted(dic.items(), key=lambda item: item[1], reverse=True)

result = []
for i in range(len(sorted_dict)):
    for _ in range(sorted_dict[i][1]):
        result.append(sorted_dict[i][0])

print(*result)
