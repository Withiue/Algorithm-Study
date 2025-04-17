#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[102][102];
int vis[102][102]; // 비에 잠긴 영역
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int n, ans;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	// 지역 높이 입력받기 (지역의 max 높이도 구하기)
	int maxh = 1;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cin>>board[i][j];
			maxh = max(maxh, board[i][j]);
		}
	}
	
	// m = 1부터 max까지 잠긴다고 반복 (점점 높이 1씩 물에 잠길거임)
	for(int m = 0; m < maxh; m++) {
		// 방문여부 초기화
		for(int i=0; i<n; i++) {
			fill(vis[i], vis[i]+n, 0);
		}
		
		// vis != 0 대상으로 bfs 돌리기
		int cnt = 0; // 물에 잠기지 않은 지역 개수 구하기
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(board[i][j] > m && vis[i][j] == 0) { //물에 안잠겼고 방문 안했으면
					// 큐에 시작점 넣고 bfs 돌리기
					queue<pair<int,int>> Q;
					Q.push({i,j});
					vis[i][j] = 1;
					cnt++; // 새로운 잠기지 않은 지역이니까 지역개수++하기
					while(!Q.empty()) {
						auto cur = Q.front(); Q.pop();
						for(int dir = 0; dir < 4; dir++) {
							int nx = cur.X + dx[dir];
							int ny = cur.Y + dy[dir];
							if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
							if(board[nx][ny] > m && vis[nx][ny] == 0) {
								Q.push({nx,ny});
								vis[nx][ny] = 1;
							}
						}
					}
				}
			}
		}
	
		// ans = 안짐긴곳 개수 최대 갱신하기
		ans = max(ans, cnt);
	}
	
	// 최대 개수 max 출력하기
	cout<<ans;
	return 0;
}