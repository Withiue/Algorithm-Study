#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[27];
int vis[27][27];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int n;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	
	for(int i=0; i<n; i++) {
		cin>>board[i];
	}
	
	int danji = 0;
	vector<int> ans;
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++) {
			if(board[i][j] == '0' || vis[i][j] == 1) continue;
			//큐에 넣기
			queue<pair<int,int>> Q; // 큐 초기화
			Q.push({i,j});
			vis[i][j] = 1;
			//단지수++
			danji++;
			int tmp = 1; //단지별집수
			//bfs 돌리기 - 단지 하나의 집 수 vector에 push_back하기
			while(!Q.empty()) {
				auto cur = Q.front(); Q.pop();
				for(int dir=0; dir<4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
					if(board[nx][ny] == '0' || vis[nx][ny] == 1) continue;
					Q.push({nx,ny});
					vis[nx][ny] = 1;
					tmp++;
				}
			}
			ans.push_back(tmp);
		}
	}
	//오름차순 정렬
	sort(ans.begin(), ans.end());
	//정답 출력
	cout<<danji<<'\n';
	for(int i=0; i<danji; i++) {
		cout<<ans[i]<<'\n';
	}
	return 0;
}