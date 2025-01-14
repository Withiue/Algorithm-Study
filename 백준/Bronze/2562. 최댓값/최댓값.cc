#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int max=0;
    int index=0;
    int num[10];
    for(int i=0; i<9; i++) {
        cin>>num[i];
        if(num[i]>max) {
            max=num[i];
            index = i+1;
        }
    }
    cout<<max<<'\n';
    cout<<index<<'\n';
}