#include <bits/stdc++.h>
using namespace std;
int N, S, temp;
vector<int> v; 
int main() {
	cin >> N >> S;
	for(int i=0; i<N; i++) {
		cin >> temp;
		v.push_back(temp);
	}
	for(int i = 0; i < N; ++i) {
        v[i] = abs(S-v[i]); // 수빈이 현재 위치 - 동생 위치의 절댓값 
    }
    sort(v.begin(), v.end(), greater<int>());
    temp = gcd(v[0], v[1]);
    for(int i = 2; i < N; ++i) {
        temp = gcd(temp, v[i]);
    }
    cout << temp;
}