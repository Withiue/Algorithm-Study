#include <bits/stdc++.h>
using namespace std;
int n, k, s, y, ans;
int grade[2][7] = {};
int main(void) {
    ios::sync_with_stdio(0), cin.tie(0);
    cin>>n>>k;
    for(int i=0; i<n; i++) {
        cin>>s>>y;
        grade[s][y]++;
    }
    
    for(int i=1; i<=6; i++) {
        if(grade[0][i]==0 && grade[1][i]==0) continue; // i학년에 아무도 없으면?
        if(grade[0][i]>0) { // i학년에 여자가 있으면
            if(grade[0][i] % k) ans += grade[0][i]/k + 1; // i학년 여자 방 갯수 구하기
            else ans += grade[0][i]/k;
        }
        if(grade[1][i]>0) { // i학년에 남자가 있으면
            if(grade[1][i] % k) ans += grade[1][i]/k + 1; // i학년 남자자 방 갯수 구하기
            else ans += grade[1][i]/k;
        }
    }

    cout<<ans;
}