#include <iostream>

using namespace std;

long long k;
long long n;
long long len[10000];

long long lines(long long l)
{
    long long result = 0;

    for (long long i = 0; i < k; i++)
        result += (len[i] / l);

    return result;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> k >> n;

    for (long long i = 0; i < k; i++)
    {
        cin >> len[i];
    }

    long long h = INT32_MAX;
    long long l = 1;
    long long m;

    while (h > l + 1)
    {
        m = (h + l) / 2;
        if (lines(m) >= n)
            l = m;
        else
            h = m;
    }

    cout << l;
}