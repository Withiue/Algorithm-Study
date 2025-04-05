#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[1002];
int fireDist[1002][1002];
int dist[1002][1002];
int r, c;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int main(void) {
    ios::sync_with_stdio(0); cin.tie(0);
    cin>>r>>c;
    // 거리 배열들 초기화하기
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            fireDist[i][j] = -1;
            dist[i][j] = -1;
        }
    }
    // 미로 값 입력받기
    for(int i = 0; i < r; i++) {
        cin >> board[i];
    }
    queue<pair<int,int>> QF; // 불 큐
    queue<pair<int,int>> QJ; // 지훈이 큐
    // 거리, 시작점 초기화
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(board[i][j] == 'F') {
                QF.push({i,j});
                fireDist[i][j] = 0;
            }
            if(board[i][j] == 'J') {
                QJ.push({i,j});
                dist[i][j] = 0;
            }
        }
    }
    // 불 bfs 구하기
    while(!QF.empty()) {
        pair<int,int> cur = QF.front(); QF.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if(nx < 0 || nx >= r || ny < 0 || ny >= c) continue; // 미로 범위 밖이면 continue
            if(board[nx][ny] == '#' || fireDist[nx][ny] >= 0) continue; // 벽이거나 이미 불이 있으면 continue
            fireDist[nx][ny] = fireDist[cur.X][cur.Y] + 1;
            QF.push({nx,ny});
        }
    }
    // 지훈이 bfs 구하기
    while(!QJ.empty()) {
        pair<int,int> cur = QJ.front(); QJ.pop();
        for(int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if(nx < 0 || nx >= r || ny < 0 || ny >= c) {  // 미로 범위 밖이면 탈출 성공이라는 의미
                cout << dist[cur.X][cur.Y] + 1;
                return 0;
            }
            if(board[nx][ny] == '#' || dist[nx][ny] >= 0) continue; // 벽이거나 / 이미 방문한 상태면 continue
            if(fireDist[nx][ny] != -1 && dist[cur.X][cur.Y] + 1 >= fireDist[nx][ny]) continue; // 불이 먼저 전파된 상태면 continue
            dist[nx][ny] = dist[cur.X][cur.Y] + 1;
            QJ.push({nx,ny});
        }
    }
    cout<< "IMPOSSIBLE"; // 중간에 탈출 못한건 탈출 불가능하다는 의미.
}