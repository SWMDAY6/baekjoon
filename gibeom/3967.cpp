#include <iostream>
#include <vector>
using namespace std;
vector<int> x_index;
vector<pair<int, int>> star_index;
char star[12];
char result[12];
bool ascii[12];
string result_str;
string str;

bool is_26(char c1, char c2, char c3, char c4)
{
    return (int)c1 - 64 + (int)c2 - 64 + (int)c3 - 64 + (int)c4 - 64 == 26;
}
void DFS(int index, int size)
{
    str = star;
    if (index != 0)
    {
        if (str.compare(result) > 0)
            return;
    }
    if (size == x_index.size())
    {
        if (!is_26(star[0], star[2], star[5], star[7]))
            return;
        if (!is_26(star[0], star[3], star[6], star[10]))
            return;
        if (!is_26(star[1], star[2], star[3], star[4]))
            return;
        if (!is_26(star[1], star[5], star[8], star[11]))
            return;
        if (!is_26(star[4], star[6], star[9], star[11]))
            return;
        if (!is_26(star[7], star[8], star[9], star[10]))
            return;
        for (int i = 0; i < 12; i++)
            result[i] = star[i];
        result_str = result;
        return;
    }

    for (int j = 0; j < 12; j++)
    {
        if (!ascii[j])
        {
            ascii[j] = true;
            star[x_index[index]] = (char)(65 + j);
            DFS(index + 1, size + 1);
            ascii[j] = false;
        }
    }
}

int main()
{
    char c;
    int index = 0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> c;
            if (c == '.')
                continue;
            star[index] = c;
            if (c == 'x')
                x_index.push_back(index);
            else
                ascii[(int)c - 65] = true;
            result[index] = 'L';
            index++;
            star_index.push_back(make_pair(i, j));
        }
    }
    result_str = result;
    DFS(0, 0);
    index = 0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (!star_index.empty())
            {
                if (star_index[0].first == i && star_index[0].second == j)
                {
                    cout << result[index++];
                    star_index.erase(star_index.begin());
                }
                else
                    cout << ".";
            }
            else
                cout << ".";
        }
        cout << endl;
    }
    return 0;
}

//출처: https://godute.tistory.com/23