#include <bits/stdc++.h>
#define MAX 8
using namespace std;
int N, M; // 1 ≤ M ≤ N ≤ 7
int sequence[MAX];
void dfs(int cnt) {
	if (cnt == M) {
		for(int index=0; index<M; index++) cout << sequence[index] << ' ';
		cout << '\n';
		return;
	} else {
		for(int index=1; index <= N; index++) {
			sequence[cnt] = index;
			dfs(cnt+1);
		}
	}
}
int main() {
	cin >> N >> M;
	dfs(0);
}