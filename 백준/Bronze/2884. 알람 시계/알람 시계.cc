#include <bits/stdc++.h>
using namespace std;
int H, M, before, after;
int main() {
	cin >> H >> M;
	before = H*60 + M;
	after = before - 45;
	if(after<0) {
		after += 24*60;
	}
	H = after / 60;
	M = after % 60;
	cout << H << " " << M;
}