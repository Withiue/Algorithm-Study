#include <bits/stdc++.h>
using namespace std;
int n;
int t[17]; // 시간
int p[17]; // 가격
int dp[17]; // dp[i]: i일부터 얻을 수 있는 최대 수익

int maxRev() {
    // 테이블 초기화
    fill(dp, dp+17, 0);

    int maxR = 0;
    
    for(int i=0; i<=n; i++) {
        // 오늘 일 안하는 경우 -> 이전의 최대수익 그대로
        dp[i] = max(dp[i], maxR);

        // 오늘 상담 하는 경우 -> 상담 끝나는날의 수익 갱신
        if(i < n && t[i] <= n - i) { // 상담이 퇴사 전에 끝나는지 확인 + i가 유효한 인덱스인지 확인
            dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i]);
        }

        maxR = max(maxR, dp[i]);
    }

    // 최대 가치 반환
    return maxR;
}

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> t[i] >> p[i];
    }

    int ans = maxRev();
    cout << ans;
    return 0;
}