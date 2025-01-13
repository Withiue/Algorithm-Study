#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int a, b, c; //주사위 값
    int reward;
    cin>>a>>b>>c;
    //1. 같은 눈 3개
    if((a==b) && (b==c)) reward = 10000 + (a*1000);
    //2. 다 다른 눈
    else if((a!=b) && (b!=c) && (c!=a)) {
        int maxNum = max({a, b, c});
        reward = maxNum*100;
    } else { //3. 같은 눈 2개
        if(a==b) reward = 1000+(a*100);
        else if(b==c) reward = 1000+(b*100);
        else if(c==a) reward = 1000+(a*100);
    }

    cout<<reward;
}