#include <iostream>

using namespace std;

int map[9][9];
int row[9][10];
int col[9][10];
int square[9][10];

void print_map()
{
    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cout << map[i][j] << " ";
        }
        cout << "\n";
    }
}

void func(int depth)
{
    if (depth == 81)
    {
        print_map();
        exit(0);
    }

    int y = depth / 9, x = depth % 9;

    if (!map[y][x])
    {
        for (int i = 1; i <= 9; ++i)
        {
            if (!row[y][i] && !col[x][i] && !square[(y / 3) * 3 + (x / 3)][i])
            {
                map[y][x] = i;
                row[y][i] = true;
                col[x][i] = true;
                square[(y / 3) * 3 + (x / 3)][i] = true;
                func(depth + 1);
                map[y][x] = 0;
                row[y][i] = false;
                col[x][i] = false;
                square[(y / 3) * 3 + (x / 3)][i] = false;
            }
        }
    }
    else
    {
        func(depth + 1);
    }
}

int main()
{
    cin.tie(false);
    ios::sync_with_stdio(NULL);

    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cin >> map[i][j];
            if (map[i][j])
            {
                row[i][map[i][j]] = true;
                col[j][map[i][j]] = true;
                square[(i / 3) * 3 + (j / 3)][map[i][j]] = true;
            }
        }
    }

    func(0);
}