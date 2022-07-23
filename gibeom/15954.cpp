#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAXVAL 123456789.0f
#define ll long long
#define ld long double

ll get_sum_in_range(const vector<ll> &psum, int a, int b)
{
    if (a == 0)
        return psum[b];
    return psum[b] - psum[a - 1];
}

ld standardDeviation(const vector<ll> &sqpsum, const vector<ll> &psum, int a, int b)
{
    ld mean = get_sum_in_range(psum, a, b) / static_cast<ld>(b - a + 1);
    ld ret = get_sum_in_range(sqpsum, a, b) - 2 * mean * get_sum_in_range(psum, a, b) + (b - a + 1) * mean * mean;
    ld variance = ret / (b - a + 1);
    return sqrt(variance);
}

int main()
{
    int nrDoll, minSub;
    cin >> nrDoll >> minSub;

    vector<ll> subsumList;
    vector<ll> sqSubsumList;

    int tmp;
    ll sum = 0;
    ll sqSum = 0;
    for (int i = 0; i < nrDoll; i++)
    {
        cin >> tmp;
        sum += tmp;
        sqSum += static_cast<ll>(tmp) * tmp;

        subsumList.push_back(sum); // 각 원소 의 부분합 , 제곱의 부분합을 미리 계산
        sqSubsumList.push_back(sqSum);
    }
    ld min_v = MAXVAL;

    for (int s = 0; s < nrDoll; s++)
    {
        for (int e = s + minSub - 1; e < nrDoll; e++)
        {
            min_v = min(min_v, standardDeviation(sqSubsumList, subsumList, s, e));
        }
    }

    cout.setf(ios::fixed);
    cout.precision(11);
    cout << min_v << endl;
    return 0;
}