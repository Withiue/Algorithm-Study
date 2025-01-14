#include <bits/stdc++.h>
using namespace std;
int sum;
int input;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int min=100;
    for(int i=0; i<7; i++) {
        cin>>input;
        if(input%2==1) {
            sum+=input;
            if(min>input) min=input;
        }
    }
    if(min==100){
        cout<<-1;
    } else {
        cout<<sum<<'\n'<<min;
    }
}