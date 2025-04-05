#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[1002][1002];
int dist[1002][1002]; // 거리가 곧 최소 일수
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int m = 0, n = 0;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	queue<pair<int,int>> Q;
	cin>>m>>n;
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			cin>>board[i][j];
			if(board[i][j] == 1) {
				Q.push({i, j});
			}
			if(board[i][j] == 0) {
				dist[i][j] = -1;
			}
		}
	}
	while(!Q.empty()) {
		pair<int,int> cur = Q.front(); Q.pop();
		for(int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
			if(dist[nx][ny] >= 0) continue;
			dist[nx][ny] = dist[cur.X][cur.Y] + 1;
			Q.push({nx, ny});
		}
	}
	int ans = 0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(dist[i][j] == -1){ // 안 익은 토마토가 있으면 -1 출력
				cout << -1;
				return 0; // 종료
			}
			ans = max(ans, dist[i][j]);
		}
	}
	cout << ans;
}