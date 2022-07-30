#include<bits/stdc++.h>
 
using namespace std;
 
#define Max 7
 
int n;
int dy[4] = { 0, 1, 0, -1 };
int dx[4] = { 1, 0, -1, 0 };
char m[Max][Max];
vector<pair<int, int> > v, t;
 
// 선생님들이 학생들을 감시할 수 있는지
// 감시할 수 있다면 true
// 감시하지 못 한다면 false
bool chk(pair<int, int> pt)
{
    for (int i = 0; i < 4; i++) {    
        
        int y = pt.first, x = pt.second; // for 문 안에 있어야 pt를 활용할 수 있다.
 
        while (0 <= y + dy[i] && y + dy[i] < n && 0 <= x + dx[i] && x + dx[i] < n)
        {
            y += dy[i];
            x += dx[i];
 
            // 장애물이면 더 이상 진행 불가능
            if (m[y][x] == 'O') {
                break;
            }
            // 학생을 발견했으면 바로 true(감시할 수 있다는 의미)
            else if (m[y][x] == 'S') {
                return true;
            }
        }
    }
 
    return false;
}
 
void simulation(int len, int idx)
{
    if (len == 3) {
        for (auto i : t) {
            // 선생님들이 단 1명이라도 감시할 수 있다면 return
            if (chk(i)) {
                return;
            }
        }
 
        // 선생님들이 1명이라도 감시하지 못 한다면 종료(장애물 3개 설치 완료)
        printf("YES\n");
        exit(0);
    }
 
    for (int i = idx; i < v.size(); i++) {
        m[v[i].first][v[i].second] = 'O'; // 장애물 설치
        simulation(len + 1, i + 1);
        m[v[i].first][v[i].second] = 'X'; // 장애물 해제
    }
}
 
int main()
{
    //freopen("C:\\Users\\park7\\Desktop\\buba.in.6", "r", stdin);
    cin.tie(0);
 
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> m[i][j];
            if (m[i][j] == 'X') {
                v.push_back({ i, j });
            }
            else if (m[i][j] == 'T') {
                t.push_back({ i, j });
            }
        }
    }
 
    simulation(0, 0);
 
    printf("NO\n");
 
    return 0;
}
