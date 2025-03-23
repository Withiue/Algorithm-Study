#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[102][102];
int dist[102][102]; // 시작점으로부터의 거리 distance
int n, m;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n>>m;
	// 거리를 -1로 초기화
	for(int i=0; i<102; i++) {
		for(int j=0; j<102; j++) {
			dist[i][j] = -1;
		}
	}
	
	//입력을 board에 채우기
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			char c;
			cin>>c;
			board[i][j] = c - '0';
		}
	}
	
	// 실행 큐에 첫 좌표를 넣기
	queue<pair<int,int>> Q;
	dist[0][0] = 1;
	Q.push({0,0});

	while(!Q.empty()) {
		// 현재 탐색할거 큐에서 꺼내 갱신
		pair<int,int> cur = Q.front(); Q.pop();
		for(int dir=0; dir<4; dir++) { // 상하좌우 돌기
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 해당 좌표가 음수이거나 최대 범위보다 크면 continue
			if(!board[nx][ny] || dist[nx][ny] > -1) continue; // 해당 좌표가 0이거나 방문했던 곳이면(거리가 -1보다 크면) continue
			Q.push({nx,ny}); // 실행 큐에 쌓기
			if(dist[nx][ny] == -1) dist[nx][ny] = dist[cur.X][cur.Y] + 1; // 거리 입력하기
		}
	}

	cout<<dist[n-1][m-1];
}