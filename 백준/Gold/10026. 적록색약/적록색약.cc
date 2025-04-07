#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
char board[102][102]; // char board 있어야함 rgb 담게
bool vis[102][102];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int n, a1, a2; // 정상인 구역 갯수는 a1, 적록색약은 a2

void bfs(int i, int j) {
	queue<pair<int,int>> Q;
	//큐 초기화 / 시작점 넣기
	Q.push({i,j});
	vis[i][j] = true;
	while(!Q.empty()) {
		auto cur = Q.front(); Q.pop();
		for(int dir = 0; dir<4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if(nx >= n || nx < 0 || ny >= n || nx < 0) continue;
			if(vis[nx][ny] || board[nx][ny] != board[i][j]) continue;
			Q.push({nx,ny});
			vis[nx][ny] = true;
		}

	}
}

int area() {
	int cnt = 0;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(!vis[i][j]) { // 방문한 적이 없으면
				// 새로운 구역이니까 구역++하고 bfs 돌기
				cnt++;
				bfs(i,j);
			}
		}
	}
	return cnt;
}

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			cin>>board[i][j];
		}
	}
	// 정상인 bfs 돌기
	int a1 = area();

	// 적록색약 bfs 돌기위한 초기화
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			// 적록색약은 빨간색==초록색임
			// board의 초록색을 빨간색으로 바꿔버리기
			if(board[i][j] == 'G') board[i][j] = 'R';
			// vis도 false로 초기화하기
			vis[i][j] = false;
		}
	}

	// 적록색약 bfs 돌기
	a2 = area();

	// 정상 / 적록색약 구역 수 공백구분출력
	cout<<a1<<' '<<a2;
	return 0;
}
