#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int board[502][502]; // 도화지 입력, 0은 색칠이 안된 부분, 1은 색칠이 된 부분
int vis[502][502]; // 색칠된 부분 중 방문했던 곳인지 여부
int n = 0, m = 0; // 도화지의 세로 크기 n, 가로 크기 m
int dx[4] = {1, 0, -1, 0}; // x, y 좌표의 상하좌우를 돌기 위한 값
int dy[4] = {0, 1, 0, -1};
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n>>m;
	for(int i=0; i<n; i++) { // board 입력받아 채우기
		for(int j=0; j<m; j++) {
			cin>>board[i][j];
		}
	}
	int cnt = 0, maxArea = 0; // 그림의 개수와 가장 넓은 그림의 넓이 변수 할당
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(board[i][j] == 0 || vis[i][j]) continue;
			cnt++; // 그림 하나 있음(그림의 시작)
			queue<pair<int,int>> Q;
			vis[i][j] = 1; // {i,j}을 방문했다고 명시
			Q.push({i,j}); // 시작점인 {i,j}을 큐에 넣는다
			int area = 0; // 지금 도는 그림의 넓이
			while(!Q.empty()) {
				area++;
				pair<int,int> cur = Q.front(); Q.pop(); // 현재 탐색할 좌표를 꺼내고 큐에서 빼낸다.
				// cout << "(" << cur.X << ", " << cur.Y << ") -> "; // 현재 탐색할 좌표 출력해보기
				for(int dir = 0; dir < 4; dir++) { // 상하좌우 칸을 살핀다.
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 밖일 경우 넘어감
					if(vis[nx][ny] || board[nx][ny] != 1) continue; // 이미 방문했거나 그림이 아닌 경우 넘어감
					vis[nx][ny] = 1; // (nx, ny)를 방문했다고 표시
					Q.push({nx, ny}); // 다음 방문할거에 (nx, ny)를 넣는다.
				}
			}
			maxArea = max(maxArea, area); // 최대 그림 넓이 갱신
		}
	}

	cout<<cnt<<"\n";
	cout<<maxArea;
}