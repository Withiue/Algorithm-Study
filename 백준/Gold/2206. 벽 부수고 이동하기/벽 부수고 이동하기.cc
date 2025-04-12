#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char board[1002][1002];
int dist[1002][1002][2];
// dist[x][y][0] : 벽을 하나도 부수지 않고 (x,y)까지 오는데 걸리는 비용
// dist[x][y][1] : 벽을 하나만 부수고 (x,y)까지 오는데 걸리는 비용, (x,y)가 벽이라서 부수는 경우 포함
int n, m;

int bfs() {
	// 초기화
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			dist[i][j][0] = dist[i][j][1] = -1;
		}
	}
	
	queue<tuple<int,int,int>> Q;
	// 큐 초기화
	Q.push({0,0,0});
	dist[0][0][0] = dist[0][0][1] = 1;

	// bfs 돌기
	while(!Q.empty()) {
		int x, y, broken;
		tie(x, y, broken) = Q.front();
		Q.pop();

		// 목표 지점에 도달했다면 거리 반환
		if(x == n-1 && y == m-1) return dist[x][y][broken];

		for(int dir = 0; dir<4; dir++) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 밖일때 continue

			// 벽이 아니고 아직 방문하지 않은 경우
			if(board[nx][ny] == '0' && dist[nx][ny][broken] == -1) {
				dist[nx][ny][broken] = dist[x][y][broken] + 1;
				Q.push({nx,ny,broken});
			}

			// 벽이고 아직 벽을 부수지 않았으며 방문하지 않은 경우
			if(!broken && board[nx][ny] == '1' && dist[nx][ny][1] == -1) {
				dist[nx][ny][1] = dist[x][y][broken] + 1;
				Q.push({nx,ny,1});
			}
		}
	}

	// 목표 지점에 도달하지 못한 경우
	return -1;
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n>>m;
	// 입력받기
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cin>>board[i][j];
		}
	}
	
	// bfs 실행하고 결과 출력
	cout<<bfs();
	return 0;

}