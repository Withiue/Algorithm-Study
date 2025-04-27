#include <bits/stdc++.h>
using namespace std;

void hanoi(int a, int b, int n) { //a는 시작 기둥, b는 도착 기둥
	if(n==1) {
		cout<<a<<' '<<b<<"\n";
		return;
	}
	hanoi(a, 6-a-b, n-1); //6-a-b는 시작기둥도 도착기둥도 아닌 기둥
	cout<<a<<' '<<b<<"\n";
	hanoi(6-a-b, b, n-1);
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int k;
	cin>>k;
	cout<<(1<<k)-1<<'\n';
	hanoi(1, 3, k);
}