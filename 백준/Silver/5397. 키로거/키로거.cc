#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	int T;
	cin>>T; //테스트 케이스 갯수 입력받기
	while(T--) {
		string input;
		cin>>input;
		list<char> result;
		list<char>::iterator cursor = result.begin();
		int len = input.length();
		for(auto c: input) {
			if(c=='<') {
				//left
				if(cursor != result.begin()) cursor--;
			} else if(c=='>') {
				//right
				if(cursor != result.end()) cursor++;
			} else if(c=='-') {
				//erase()
				if(cursor != result.begin()) {
					cursor--;
					cursor = result.erase(cursor);
				}
			} else {
				//insert();
				cursor = result.insert(cursor, c);
				cursor++;
			}
		}
		for(auto c: result) cout<<c;
		cout<<'\n';
	}
}