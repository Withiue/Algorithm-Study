//어려워서 챗지피티 참고함ㅠ 스택을 사용하면 쉽게 풀리는 문제였다! 
#include <bits/stdc++.h>
using namespace std;
int T;
bool isVPS(const string& s) { //고정된 문자열의 주소를 가져온다. 
	stack<int> stk;
	for(char ch : s) { //문자열의 문자를 하나하나씩 돈다. 
		if (ch == '(') { //(면 stack 하나를 쌓는다. 
			stk.push(ch);
		} else if (ch == ')') { //)면 stack 하나를 꺼낸다. 
			if (stk.empty()) { //stack이 비었다면 
				return false; //VPS가 아니다. 
			} else {
				stk.pop(); 
			}
		}
	}
	return stk.empty(); //stack이 비었으면 true, 안비었으면 false를 return한다. 
}
int main() {
	cin >> T;
	for(int i=0; i<T; i++) {
		string text;
		cin >> text;
		if (isVPS(text)) {
			cout << "YES" << "\n";
		} else {
			cout << "NO" << "\n";
		}
	}
	return 0;
}