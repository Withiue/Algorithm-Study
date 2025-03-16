#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	while(true) {
		string line;
		getline(cin, line);
		if(line == ".") break;
		stack<char> stk;
		bool isValid = true;
		for(auto c : line) {
			if (c == '(' || c == '[') {
				stk.push(c);
			} else if(c == ')') {
				if(stk.empty() || stk.top() != '(') {
					isValid = false;
					break;
				}
				stk.pop();
			} else if(c == ']') {
				if(stk.empty() || stk.top() != '[') {
					isValid = false;
					break;
				}
				stk.pop();
			}
		}
		if(!stk.empty()) isValid = false;
		if(isValid) cout << "yes\n";
		else cout<<"no\n";
	}
}