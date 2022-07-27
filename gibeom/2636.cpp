#include <iostream>
#include <queue>
#include <cstring>

using namespace std;
int r, c;
char board[100][100];
bool visited[100][100];
int dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
int result, time;

bool bfs()
{
    visited[0][0] = true;
    int cnt = 0;
    queue<pair<int, int>> q;
    q.push({0, 0});
    time++;
    while (!q.empty())
    {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nr = r + dir[i][0];
            int nc = c + dir[i][1];
            if (nr >= 0 && nr < r && nc >= 0 && nc < c && !visited[nr][nc])
            {

                if (board[nr][nc] == '0')
                {
                    q.push({nr, nc});
                }

                else
                {
                    board[nr][nc] = '0';
                    cnt++;
                }
                visited[nr][nc] = true;
            }
        }
    }

    if (cnt == 0)
    {
        cout << --time << '\n'
             << result;
        return true;
    }

    else
    {
        result = cnt;
        return false;
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> r >> c;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> board[i][j];
        }
    }

    while (true)
    {
        if (bfs())
            break;
        memset(visited, false, sizeof(visited));
    }
}