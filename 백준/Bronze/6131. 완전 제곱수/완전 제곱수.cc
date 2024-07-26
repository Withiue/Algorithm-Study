#include <bits/stdc++.h>
using namespace std;
int N, result;
int main() {
	cin >> N;
	//A^2 = B^2 + N
	//1 ≤ B ≤ A ≤ 500
	for(int A = 1; A <= 500; A++) {
		for (int B = 1; B <= 500; B++) {
			if (pow(A,2) == pow(B,2) + N && B <= A) {
				result++;	
			}
		}
	}
	cout << result;
	return 0;
}