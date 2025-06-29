#include <bits/stdc++.h>
using namespace std;
int n;
char board[2200][2200];

void star(int n, int y, int x) {
	// 0. n==1이면 return; (재귀 탈출)
	if(n==1) {
		return;
	} else { // 1. n!=1이면
		// 	1-1. 가운데 공백으로 채우기
		for(int i=y+n/3; i<y+n/3*2; i++) {
			for(int j=x+n/3; j<x+n/3*2; j++) {
				board[i][j] = ' ';
			}
		}
		// 	1-2. 나머지 8개 재귀함수 실행
		star(n / 3, y, x);
		star(n / 3, y, x + n/3);
		star(n / 3, y, x + n/3*2);
		star(n / 3, y + n/3, x);
		star(n / 3, y + n/3, x + n/3 * 2);
		star(n / 3, y + n/3 * 2, x);
		star(n / 3, y + n/3 * 2, x + n/3);
		star(n / 3, y + n/3 * 2, x + n/3 * 2);
	}
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	// 1. 입력받기
	cin>>n;
	// 2. board를 모두 *로 초기화하기
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			board[i][j] = '*';
		}
	}
	// 3. 재귀함수 실행
	star(n, 0, 0);
	// 4. 별 출력
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cout<<board[i][j];
		}
		cout<<'\n';
	}
}