#include <bits/stdc++.h>
using namespace std;
int dist[1000002];
int f, s, g, u, d;
// 꼭대기/현재/가야하는/위로/아래로

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>f>>s>>g>>u>>d;
	int dx[2] = {u, -d};
	fill(dist, dist+f+1, -1);
	queue<int> Q;
	Q.push(s);
	dist[s] = 0;
	while(!Q.empty()) {
		auto cur = Q.front(); Q.pop();
		for(int dir = 0; dir<2; dir++) {
			int nx = cur + dx[dir];
			if(nx < 1 || nx > f) continue;
			if(dist[nx] == -1) {
				Q.push(nx);
				dist[nx] = dist[cur] + 1;
			}
		}
	}
	if(dist[g] == -1) {
		cout<<"use the stairs";
	} else {
		cout<<dist[g];
	}
	return 0;
}
