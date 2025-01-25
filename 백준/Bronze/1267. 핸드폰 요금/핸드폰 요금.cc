#include <bits/stdc++.h>
using namespace std;

int calculatePrice(int inputTime, int divTime, int money) {
    int sum = (inputTime / divTime + 1) * money;
    return sum;
}
int main(void) {
    int N;
    int Y = 0; 
    int M = 0;
    cin>>N;
    int time[N];
    for(int i=0; i<N; i++) cin>>time[i];
    for(int i=0; i<N; i++) Y += calculatePrice(time[i], 30, 10);
    for(int i=0; i<N; i++) M += calculatePrice(time[i], 60, 15);

    if(Y < M) {
        cout<<'Y'<<' '<<Y;
    } else if(M < Y) {
        cout<<'M'<<' '<<M;
    } else cout<<'Y'<<' '<<'M'<<' '<<Y;
}
