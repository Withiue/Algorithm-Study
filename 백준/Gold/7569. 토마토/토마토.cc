#include <bits/stdc++.h>
using namespace std;
int board[102][102][102];
int dist[102][102][102];
int dx[6] = {0, 1, 0, -1, 0, 0};
int dy[6] = {1, 0, -1, 0, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};
int n, m, h; // m: 가로, n: 세로, h: 높이
int day;
queue<tuple<int,int,int>> Q;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin>>m>>n>>h;
    // 토마토 입력받기
    for(int i=0; i<h; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                int tmp;
                cin>>tmp;
                board[j][k][i] = tmp;
                // 익은 토마토면 Q에 넣기 (여러 개의 시작점)
                if(tmp == 1) Q.push({j,k,i});
                if(tmp == 0) dist[j][k][i] = -1; // dist -1로 초기화하기
            }
        }
    }

    // bfs 돌기
    while(!Q.empty()) {
        auto cur = Q.front(); Q.pop();
        int curX, curY, curZ;
        tie(curX, curY, curZ) = cur;
        for(int dir = 0 ; dir<6; dir++) {
            int nx = curX + dx[dir];
            int ny = curY + dy[dir];
            int nz = curZ + dz[dir];
            if(nx >= n || nx < 0 || ny >= m || ny < 0 || nz >= h || nz < 0) continue;
            if(dist[nx][ny][nz] != -1) continue;
            dist[nx][ny][nz] = dist[curX][curY][curZ] + 1;
            Q.push({nx,ny,nz});
        }
    }
    
    // for문 돌면서 dist값 max 갱신
    for(int i=0; i<h; i++) {
        for(int j=0; j<n; j++) {
            for(int k=0; k<m; k++) {
                if(dist[j][k][i] == -1) {
                    cout<<-1;
                    return 0;
                }
                day = max(day, dist[j][k][i]);
            }
        }
    }
    cout<<day;
    return 0;
}