#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    int roomNum;
    cin >> roomNum;
    int num;
    int arr[9] = {};
    while(roomNum>0) {
        if(roomNum%10 == 9) {
            arr[6]++;
        } else arr[roomNum%10]++;
        roomNum /= 10;
    }
    if(arr[6]%2==0) { // 6, 9의 갯수가 짝수일때
        arr[6] /= 2;
    } else { // 홀수일때
        arr[6] = (arr[6] / 2) + 1;
    }
    int max = 0;
    for(int i=0; i<9; i++) {
        if(max<arr[i]) {
            max = arr[i];
        }
    }
    cout << max;
}