#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <queue>
#include <cstring>

using namespace std;

const int INF = 987654321;
const int MAX = 125 + 1;

typedef struct
{
    int y, x;
} Dir;

Dir moveDir[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int graph[MAX][MAX];
int dist[MAX][MAX];
bool visited[MAX][MAX];

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int cnt = 1;
    while (true)
    {
        int N;
        cin >> N;

        if (N == 0)
            break;

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                dist[i][j] = INF;

        memset(visited, false, sizeof(visited));

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                cin >> graph[i][j];

        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

        pq.push({0, {0, 0}});
        visited[0][0] = true;

        while (!pq.empty())

        {
            int y = pq.top().second.first;
            int x = pq.top().second.second;

            int cost = pq.top().first;

            pq.pop();

            for (int i = 0; i < 4; i++)
            {
                int nextY = y + moveDir[i].y;

                int nextX = x + moveDir[i].x;

                int nextCost = cost + graph[nextY][nextX];

                if (0 <= nextY && nextY < N && 0 <= nextX && nextX < N)

                    if (!visited[nextY][nextX] && dist[nextY][nextX] > nextCost)
                    {
                        visited[nextY][nextX] = true;

                        dist[nextY][nextX] = nextCost;

                        pq.push({nextCost, {nextY, nextX}});
                    }
            }
        }

        cout << "Problem " << cnt++ << ": " << graph[0][0] + dist[N - 1][N - 1] << "\n";
    }
}