#include <bits/stdc++.h>
using namespace std;
int N;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin>>N;

    for(int i=1; i<=N-1; i++) {
        for(int j=1; j<=i; j++) cout<<"*";
        for(int j=0; j<(N-i)*2; j++) cout<<" ";
        for(int j=1; j<=i; j++) cout<<"*";
        cout<<'\n';
    }

    for(int i=1; i<=N; i++) { //i=1~5
        for(int j=N; j>=i; j--) cout<<'*'; //j=5~1
        for(int j=0; j<2*(i-1); j++) cout<<' '; //j=0,2,4,6,8
        for(int j=N; j>=i; j--) cout<<'*'; //j=5~1
        cout<<'\n';
    }
}