#include <bits/stdc++.h>
using namespace std;
int K, a, ans;

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	stack<int> stk;
	cin>>K;
	while(K--) {
		cin>>a;
		if(a==0) stk.pop();
		else stk.push(a);
	}

	while(!stk.empty()) {
		ans+=stk.top();
		stk.pop();
	}
	cout<<ans;
}