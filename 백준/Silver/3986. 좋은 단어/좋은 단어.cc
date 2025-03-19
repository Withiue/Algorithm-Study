#include <bits/stdc++.h>
using namespace std;
int n, cnt;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	while(n--){
		string s;
		stack<char> stk;
		cin>>s;
		for(char c : s) {
			if(c == 'A') {
				if(stk.empty()) stk.push(c);
				else if(stk.top() == 'A') stk.pop();
				else stk.push(c);
			} else if(c == 'B') {
				if(stk.empty()) stk.push(c);
				else if(stk.top() == 'B') stk.pop();
				else stk.push(c);
			}	
		}
		if(stk.empty()) cnt++;
	}
	cout<<cnt;
}