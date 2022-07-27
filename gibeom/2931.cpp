#include <iostream>
#include <queue>
using namespace std;
int r, c;
int erasedX, erasedY;
char map[26][26];
bool blockch[26][26];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
queue<pair<int, int>> q;
bool ch[26][26] = {
    0,
};
void bfs(int mx, int my, int zx, int zy)
{
    q.push(make_pair(mx, my));
    q.push(make_pair(zx, zy));
    ch[mx][my] = true;
    ch[zx][zy] = true;
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && ny >= 0 && nx < r && ny < c && !ch[nx][ny])
            {
                if (map[x][y] == 'M' || map[x][y] == 'Z')
                {
                    if (map[nx][ny] == '.')
                        continue;
                }
                else if (map[x][y] == 124)
                {
                    if (i == 2 || i == 3)
                        continue;
                }
                else if (map[x][y] == '-')
                {
                    if (i == 0 || i == 1)
                        continue;
                }
                else if (map[x][y] == '1')
                {
                    if (i == 0 || i == 2)
                        continue;
                }
                else if (map[x][y] == '2')
                {
                    if (i == 1 || i == 2)
                        continue;
                }
                else if (map[x][y] == '3')
                {
                    if (i == 1 || i == 3)
                        continue;
                }
                else if (map[x][y] == '4')
                {
                    if (i == 0 || i == 3)
                        continue;
                }
                if (map[nx][ny] == '.')
                {
                    erasedX = nx;
                    erasedY = ny;
                    return;
                }
                q.push(make_pair(nx, ny));
                ch[nx][ny] = true;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> r >> c;
    int mx, my, zx, zy;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 'M')
            {
                mx = i;
                my = j;
            }
            else if (map[i][j] == 'Z')
            {
                zx = i;
                zy = j;
            }
        }
    }
    bfs(mx, my, zx, zy);
    char block[7] = {124, '-', '+', '1', '2', '3', '4'};
    bool blockCh[7] = {1, 1, 1, 1, 1, 1, 1};
    for (int i = 0; i < 7; i++)
    {
        if (i == 0 || i == 2 || i == 4 || i == 5)
        {
            int nx = erasedX + dx[0];
            int ny = erasedY + dy[0];
            if (map[nx][ny] == '.' || map[nx][ny] == '-' || map[nx][ny] == '2' || map[nx][ny] == '3' || nx < 0 || ny < 0 || nx >= r || ny >= c)
                blockCh[i] = false;
        }
        if (i == 0 || i == 2 || i == 3 || i == 6)
        {
            int nx = erasedX + dx[1];
            int ny = erasedY + dy[1];
            if (map[nx][ny] == '.' || map[nx][ny] == '-' || map[nx][ny] == '1' || map[nx][ny] == '4' || nx < 0 || ny < 0 || nx >= r || ny >= c)
                blockCh[i] = false;
        }
        if (i == 1 || i == 2 || i == 5 || i == 6)
        {
            int nx = erasedX + dx[2];
            int ny = erasedY + dy[2];
            if (map[nx][ny] == '.' || map[nx][ny] == 124 || map[nx][ny] == '3' || map[nx][ny] == '4' || nx < 0 || ny < 0 || nx >= r || ny >= c)
                blockCh[i] = false;
        }
        if (i == 1 || i == 2 || i == 3 || i == 4)
        {
            int nx = erasedX + dx[3];
            int ny = erasedY + dy[3];
            if (map[nx][ny] == '.' || map[nx][ny] == 124 || map[nx][ny] == '1' || map[nx][ny] == '2' || nx < 0 || ny < 0 || nx >= r || ny >= c)
                blockCh[i] = false;
        }
    }
    if (blockCh[2])
        cout << erasedX + 1 << ' ' << erasedY + 1 << ' ' << block[2] << '\n';
    else
    {
        for (int i = 0; i < 7; i++)
            if (blockCh[i])
            {
                cout << erasedX + 1 << ' ' << erasedY + 1 << ' ' << block[i] << '\n';
            }
    }
}

//출처: https://chogyujin.github.io/2019/04/11/BOJ-2931%EB%B2%88-%EA%B0%80%EC%8A%A4%EA%B4%80/