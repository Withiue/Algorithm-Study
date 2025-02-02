#include <bits/stdc++.h>
using namespace std;
int main(void) {
    int n, v, k;
    int a[201] = {};
    cin>>n;
    for(int i=0; i<n; i++) {
        cin>>k;
        a[k+100]++;
    }
    cin>>v;
    cout<<a[v+100];
}