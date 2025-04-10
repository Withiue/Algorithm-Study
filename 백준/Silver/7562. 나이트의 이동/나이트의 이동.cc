#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[302][302];
int dist[302][302];
int dx[8] = { -2, -2, -1, -1, 1, 1, 2, 2 }; // 여덟 방향으로 움직일 수 있음
int dy[8] = { 1, -1, 2, -2, 2, -2, 1, -1 };
int t; // 테스트 케이스
queue<pair<int,int>> Q;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>t;	
	while(t--) {
		int ans = 0, l = 0;
		pair<int,int> now, goal;
		cin>>l;
		//초기화
		for(int i=0; i<302; i++) {
			fill(board[i], board[i]+302, 0);
			fill(dist[i], dist[i]+302, -1);
		}
		//시작점
		cin>>now.X>>now.Y;
		dist[now.X][now.Y] = 0;
		Q.push({now.X,now.Y});
		
		cin>>goal.X>>goal.Y;
		
		while(!Q.empty()) {
			auto cur = Q.front(); Q.pop();
			for(int dir=0; dir<8; dir++) {
				int nx = cur.X + dx[dir];
				int ny = cur.Y + dy[dir];
				if(nx >= l || nx < 0 || ny >= l || ny < 0) continue;
				if(dist[nx][ny] >= 0) continue;
				dist[nx][ny] = dist[cur.X][cur.Y] + 1;
				Q.push({nx,ny});
			}
		}
		cout<<dist[goal.X][goal.Y]<<'\n';
	}
}