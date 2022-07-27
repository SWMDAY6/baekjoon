from collections import defaultdict
s = [list(str(input())) for _ in range(5)]
star = ['' for _ in range(12)]
idx = 0
visited = defaultdict(bool)
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            star[idx] = s[i][j]
            idx += 1
            if s[i][j] != 'x':
                visited[s[i][j]] = True
apb = [chr(i) for i in range(ord('A'), ord('L')+1)]


def chk():
    if not (ord(star[0]) + ord(star[2]) + ord(star[5]) + ord(star[7]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[2]) + ord(star[3]) + ord(star[4]) == 22 + ord('A')*4):
        return False
    if not (ord(star[0]) + ord(star[3]) + ord(star[6]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[7]) + ord(star[8]) + ord(star[9]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[5]) + ord(star[8]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    if not (ord(star[4]) + ord(star[6]) + ord(star[9]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    return True


ans = []
flag = False


def magic_star(cur, mstar,):
    global ans, flag
    if flag:
        return
    if cur == 12:
        if chk():
            flag = True
            ans = mstar[:]
        return
    if mstar[cur] != 'x':
        magic_star(cur+1, mstar)
    else:
        for i in range(len(apb)):
            if not visited[apb[i]]:
                mstar[cur] = apb[i]
                visited[apb[i]] = True
                magic_star(cur+1, mstar)
                visited[apb[i]] = False
                mstar[cur] = 'x'
                if flag:
                    return


magic_star(0, star)
idx = 0
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            s[i][j] = ans[idx]
            idx += 1
for i in range(5):
    print(''.join(s[i]))
