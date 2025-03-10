#include <bits/stdc++.h>
using namespace std;

void parse(string& tmp, deque<int>& d) {
	int cur = 0; // 현재 숫자
	for(int i=1; i < tmp.size()-1; i++) { // 문자열의 첫 '[' 와 마지막 ']'를 제외하고 순회
		if(tmp[i] == ',') {
			d.push_back(cur);
			cur = 0;
		} else { // 숫자 문자를 만나면
			cur = 10 * cur + (tmp[i] - '0'); //(tmp[i] - '0')는 1의 자릿수 계산, 142계산하면 1, 14 순으로 커서에 쌓임
		}
	}
	if(cur != 0) { //마지막 숫자 처리
		d.push_back(cur);
	}
}

void print_result(deque<int>& d) {
	cout<<'[';
	for(int i=0; i<d.size(); i++) {
		cout<<d[i];
		if(i != d.size()-1) {
			cout <<",";
		}
	}
	cout<<"]\n";
}

int t;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	
	
	cin>>t;
	
	while(t--) {
		deque<int> d;
		int rev = 0; //뒤집기 상태 플래그 (0은 정상, 1은 뒤집힌 상태)
		int n;
		bool isWrong = false;
		
		string query, tmp;
		cin>>query;
		cin>>n;
		cin>> tmp;

		parse(tmp, d);

		for(char c : query) {
			if(c=='R') {
				rev = 1 - rev;
			} else if(c=='D') {
				if(d.empty()) {
					isWrong = true;
					break;
				}
				if(!rev) d.pop_front();
				else d.pop_back();
			}
		}

		if(isWrong) {
			cout<<"error\n";
		} else {
			if(rev) reverse(d.begin(), d.end()); //최종적으로 뒤집기 상태면 덱을 실제로 뒤집음
			print_result(d);
		}
	}

}