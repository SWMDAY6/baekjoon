#include <bits/stdc++.h>
using namespace std;
#define w first
#define p second

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, w, l;
    cin >> n >> w >> l;
    queue<int> truck;
    for (int i = 0; i < n; i++)
    {
        int w;
        cin >> w;
        truck.push(w);
    }
    deque<pair<int, int>> bridge;
    int time = 0;
    while (!truck.empty() || !bridge.empty())
    {
        for (int i = 0; i < bridge.size(); i++)
            bridge[i].p -= 1;
        if (!bridge.empty() && bridge.front().p == 0)
            bridge.pop_front();
        int weight = 0;
        for (auto truck : bridge)
            weight += truck.w;
        if (!truck.empty() && truck.front() + weight <= l && bridge.size() < w)
        {
            bridge.push_back({truck.front(), w});
            truck.pop();
        }
        time++;
    }
    cout << time;
}
