#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int avg;
    int sum=0;
    int n[5];
    for(int i=0; i<5; i++) {
        cin>>n[i];
        sum+=n[i];
    }
    avg = sum/5;
    sort(n, n+5);
    cout<<avg<<'\n';
    cout<<n[2]<<'\n';
}