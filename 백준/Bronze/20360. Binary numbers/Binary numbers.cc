#include <bits/stdc++.h>
using namespace std;
long long n;
int main() {
	cin >> n;
	bitset<20> binary(n); // 20비트 이진수로 변환
	
	// 비트셋에서 1인 위치를 찾아 출력 
	bool first = true;
	for (int i=0; i < 20; i++) {
		if (binary[i]) {
			if (!first) { //첫 1이 아니면 공백 출력 
				cout << " ";
			}
			cout << i;
			first = false;
		}
	}
	return 0; 
}