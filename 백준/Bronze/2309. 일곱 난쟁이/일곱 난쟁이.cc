#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int a9[9];
    int sum=0;
    for(int i=0; i<9; i++) {
        cin>>a9[i];
        sum += a9[i];
    }
    bool found(false);
    for(int i=0; i<8; i++) {
        if(found) break;
        for(int j=i+1; j<9; j++) {
            if(a9[i]+a9[j] == sum - 100) {
                a9[i] = 1000;
                a9[j] = 1000; //큰 수 아무거나 할당하기
                found = true;
                break;
            }
        }
    }
    sort(a9, a9+9);
    for(int i=0; i<7; i++) cout<<a9[i]<<'\n';
}