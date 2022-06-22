def draw(n):
    if n == 1:
        return ['*']
    
    stars = draw(n//3)
    l = []

    for star in stars:
        l.append(star*3)
    for star in stars:
        l.append(star + ' '*(n//3) + star)
    for star in stars:
        l.append(star*3)
    
    return l

n = int(input())
print('\n'.join(draw(n)))
