#include <bits/stdc++.h>
using namespace std;
int n;
int board[2200][2200];
int cnt[3]; // -1, 0, 1로 채워진 종이 갯수

bool isSame(int x, int y, int n) {
    for(int i=x; i<x+n; i++) {
        for(int j=y; j<y+n; j++) {
            if(board[x][y] != board[i][j]) return false;
        }
    }
    return true;
}

void func(int x, int y, int z) {
    // base condition
    //만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
    if(isSame(x, y, z)) {
        cnt[board[x][y] + 1] += 1;
        return;
    }
    //(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
    int n = z / 3;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            func(x + i * n, y + j * n, n);
        }
    }
}

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin>>n;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin>>board[i][j];
        }
    }

    func(0, 0, n);

    for(int i=0; i<3; i++) cout<<cnt[i]<<"\n";
}