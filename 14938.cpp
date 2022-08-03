#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

int board[102][102];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int region;
    int dist;
    int road;

    cin >> region >> dist >> road;
    vector<int> v(region + 1);

    for (int i = 1; i <= region; i++)
        cin >> v[i];

    for (int i = 0; i <= region; i++)
    {
        for (int j = 0; j <= region; j++)
        {
            if (i == j)
                board[i][j] = 0;
            else
                board[i][j] = 1e9;
        }
    }

    for (int i = 0; i < road; i++)
    {
        int from, to, dist;
        cin >> from >> to >> dist;
        board[from][to] = dist;
        board[to][from] = dist;
    }

    for (int k = 1; k <= region; k++)
    {
        for (int i = 1; i <= region; i++)
        {
            for (int j = 1; j <= region; j++)
            {
                if (board[i][j] > board[i][k] + board[k][j])
                {
                    board[i][j] = board[i][k] + board[k][j];
                }
            }
        }
    }

    int result = -1;

    for (int i = 1; i <= region; i++)
    {
        int sum = 0;
        for (int j = 1; j <= region; j++)
        {
            if (board[i][j] <= dist)
            {
                sum += v[j];
            }
        }
        result = max(result, sum);
    }

    cout << result;
}