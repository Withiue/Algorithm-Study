#include <bits/stdc++.h>
using namespace std;
int n, b;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	queue<int> Q;
	for(int i=1; i<=n; i++) Q.push(i);
	while(n!=1) {
		Q.pop();
		b = Q.front();
		Q.pop();
		Q.push(b);
		n--;
	}
	cout<<Q.front();
}