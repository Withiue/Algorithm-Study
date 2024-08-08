#include <bits/stdc++.h>
using namespace std;
int main()
{
    int N;
    cin >> N;

    int arr[1001];
    for (int i = 1; i <= N; i++)
        scanf("%d", &arr[i]);

    int dp[1001];
    for (int i = 1; i <= N; i++)
        dp[i] = 1;

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j < i; j++) {
            if(arr[i] > arr[j]) { // 후의 숫자가 전의 숫자보다 큰 경우 
                dp[i] = max(dp[i], dp[j]+1); // i번째(후의 숫자) dp를 갱신한다. 
            }
        }
    }
    sort(dp, dp+N+1);
    printf("%d",dp[N]);
}