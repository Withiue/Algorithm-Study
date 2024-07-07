#include <bits/stdc++.h>
using namespace std;
int N, M;
int main() {
	cin >> N >> M;
	int A[N][M];
	int B[N][M];
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			cin >> A[i][j];
		}
	}
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			cin >> B[i][j];
		}
	}
	
	int add[N][M];
	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			add[i][j] = A[i][j] + B[i][j];
		}
	}
	
	for (int i=0; i<N; i++) {
		for (int j=0; j<M; j++) {
			cout << add[i][j] << " ";
		}
		cout << endl;
	}
}