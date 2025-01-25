#include <bits/stdc++.h>
using namespace std;
int a, b;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int card[20];
    for(int i=0; i<20; i++) card[i] = i+1;
    for(int i=0; i<10; i++) {
        cin>>a>>b;
        if(a==b) continue;
        else {
            while(a<b) {
                swap(card[a-1], card[b-1]);
                a++;
                b--;
            }
        }
    }
    for(int i=0; i<20; i++) cout<<card[i]<<' ';
}