#include <bits/stdc++.h>
using namespace std;
int n, m;
int max_value = 0;
int main() {
	int in[9][9];
	for (int i=0; i<9; i++) {
		for (int j=0; j<9; j++) {
			cin >> in[i][j];
		}
	}
	for (int i=0; i<9; i++) {
		for (int j=0; j<9; j++) {
			if(in[i][j] >= max_value) {
				max_value = in[i][j];
				n = i+1;
				m = j+1;
			}
		}
	}
	cout << max_value << "\n" << n << ' ' << m;
}