#include <bits/stdc++.h>
using namespace std;

const int MX = 600005;
char dat[MX];
int pre[MX];
int nxt[MX];
int unused = 1;
int M;
char a, b;

void insert(int addr, char alphabet) {
	dat[unused] = alphabet;
	pre[unused] = addr;
	nxt[unused] = nxt[addr];
	if(nxt[addr] != -1) pre[nxt[addr]] = unused;
	nxt[addr] = unused;
	unused++;
}

void erase(int addr) {
	nxt[pre[addr]] = nxt[addr];
	if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
}

void traverse() {
	int cur = nxt[0];
	while(cur!=-1) {
		cout<<dat[cur];
		cur = nxt[cur];
	}
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	fill(pre, pre+MX, -1);
	fill(nxt, nxt+MX, -1);
	// 첫 문자열 입력받기
	string str;
	cin >> str;
	int cursor=0;
	// linked list에 문자열 추가하기
	for(auto c: str) {
		insert(cursor, c);
		cursor++;
	}
	// 명령어 갯수 M 입력받기
	cin >> M;
	// M만큼 반복하면서 입력받기
	for(int i=0; i<M; i++) {
		cin >> a; // 명령어 입력받기
		if(a=='P') { // 문자를 커서 왼쪽에 추가
			cin >> b; // 추가할 문자 입력받기
			insert(cursor, b);
			cursor = nxt[cursor]; // 다음 노드로 이동
		} else if(a=='D') { // 커서 오른쪽으로 옮김, 커서가 맨뒤면 무시
			if(nxt[cursor] != -1) cursor = nxt[cursor];
		} else if(a=='L') { // 커서 왼쪽으로 옮김, 커서가 맨앞이면 무시
			if(pre[cursor] != -1) cursor = pre[cursor];
		} else if(a=='B') { // 커서 왼쪽 문자 삭제, 커서가 맨앞이면 무시
			if(pre[cursor] != -1) {
				erase(cursor);
				cursor = pre[cursor];
			}
		}
	}
	// 편집된 문자열 출력하기
	traverse();
}