#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[52][52]; // 배추밭에 배추가 있으면 1, 아니면 0
int vis[52][52]; // 지렁이가 방문했으면 1, 아니면 0
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int n, m, t, k;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>t;
	while(t--) {
		cin>>m>>n>>k;
		int x, y;
		for(int i=0; i<k; i++) { // 배추 있는 곳 입력받기
			cin>> x >> y;
			board[y][x] = 1;
		}
		int num = 0; // 지렁이 수
		for(int i=0; i<n; i++) { 
			for(int j=0; j<m; j++) {
				if(board[i][j] == 0 || vis[i][j]) continue; // 배추가 없거나 이미 방문했으면 continue
				num++;
				queue<pair<int,int>> Q;
				vis[i][j] = 1;
				Q.push({i,j}); // 첫 배추 시작점 입력받기
				while(!Q.empty()) { // 지렁이 bfs 돌기
					pair<int,int> cur = Q.front(); Q.pop();
					for(int dir = 0; dir<4; dir++) {
						int nx = cur.X + dx[dir];
						int ny = cur.Y + dy[dir];
						if(nx >= n || nx < 0 || ny >= m || ny < 0) continue; // 방문해야하는 곳이 범위 밖이면 continue
						if(vis[nx][ny] || board[nx][ny] != 1) continue; // 이미 방문했거나 배추가 없으면 continue
						vis[nx][ny] = 1;
						Q.push({nx,ny});
					}
				}
	
			}
		}
		// 답 출력
		cout<<num<<'\n';
		// 배열 초기화 후 다음 테스트 케이스
		for(int i=0; i<n; i++) {
			fill(board[i], board[i]+m, 0);
			fill(vis[i], vis[i]+m, 0);
		}
	}
}
