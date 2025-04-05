#include <bits/stdc++.h>
using namespace std;
#define X first;
#define Y second;
int vis[100002];
int n, k;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	fill(vis, vis+100002, -1); // -1로 초기화
	cin>>n>>k;
	queue<int> Q;
	Q.push(n);
	vis[n] = 0; // 시간 초기화
	while(vis[k] == -1) {
		int cur = Q.front(); Q.pop();
		int dx[3] = {-1, 1, cur};
		for(int dir=0; dir<3; dir++) {
			int nx = cur + dx[dir];
			if(nx < 0 || nx > 100000) continue; // 수빈이가 범위 밖이면 continue
			if(vis[nx] != -1) continue; // 수빈이가 이미 방문했던 위치면 continue
			vis[nx] = vis[cur] + 1;
			Q.push(nx);
		}
	}
	cout << vis[k];
}