#include <bits/stdc++.h>
using namespace std;
int n;
int board[66][66];

void QuadTree(int n, int y, int x) {
	// 0. n==1이면 입력값 바로 출력
	if(n==1) {
		cout<<board[y][x];
		return;
	}
	// 1. 모두다 0 혹은 모두다 1인지 확인
	bool zero=true, one=true;
	for(int i=y; i<y+n; i++) {
		for(int j=x; j<x+n; j++) {
			if(board[i][j])
			zero = false;
			else
			one = false;
		}
	}
	// 1-1. 모두 다 같다면 그대로 출력하기
	if(zero) {
		cout<<0;
	} else if(one) {
		cout<<1;
	} else {
		// 1-2. 아니라면 4분할 해서 4개의 QuadTree함수 돌리기.
		cout<<"(";
		QuadTree(n / 2, y, x); // 왼쪽 위
		QuadTree(n / 2, y, x + n / 2); // 오른쪽 위
		QuadTree(n / 2, y + n / 2, x); // 왼쪽 아래
		QuadTree(n / 2, y + n / 2, x + n / 2); // 오른쪽 아래
		cout<<")";
	}
	return;
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	for(int i=0; i<n; i++) {
		string line;
		cin>>line;
		for(int j=0; j<n; j++) {
			board[i][j] = line[j] - '0';
		}
	}
	QuadTree(n, 0, 0);
}