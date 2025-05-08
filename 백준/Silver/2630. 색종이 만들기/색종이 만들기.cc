#include <bits/stdc++.h>
using namespace std;
int n;
int board[130][130];
int cnt[2]; //하얀색, 파란색 순서대로 담기

bool isSame(int x, int y, int n) {
	for(int i=x; i<x+n; i++) {
		for(int j=y; j<y+n; j++) {
			if(board[i][j] != board[x][y]) return false;
		}
	}
	return true;
}

void foo(int x, int y, int z) {
	//base condition
	// 모두 같은 숫자거나 쪼갤 게 없으면 멈추기
	if(isSame(x, y, z) == true || z == 1) {
		cnt[board[x][y]] += 1;
		return;
	}

	// 재귀
	// 종이를 4분할로 자르고, 각각의 범위에 대해 재귀함수 호출
	int n = z / 2;
	for(int i=0; i<2; i++) {
		for(int j=0; j<2; j++) {
			foo(x + i * n, y + j * n, n);
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

	foo(0, 0, n);

	cout<<cnt[0]<<"\n"<<cnt[1];
}