#include <bits/stdc++.h>
using namespace std;

// 변수 초기화
int N, X, A[10005];
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    // 첫째 줄 입력받기
    cin >> N >> X;
    
    // 배열 A 입력 받아서 초기화
    for(int i=0; i<N; i++) cin >> A[i];
    for(int i=0; i<N; i++) {
        if(A[i]<X) cout << A[i] << ' ';
    }
}