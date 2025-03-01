#include <bits/stdc++.h>
using namespace std;
int n;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	deque<int> dq;
	string m;
	cin>>n;
	int a;
	while(n--) {
		cin>>m;
		if(m=="push_front") {
			cin>>a;
			dq.push_front(a);
		} else if(m=="push_back") {
			cin>>a;
			dq.push_back(a);
		} else if(m=="pop_front") {
			if(dq.empty()) cout<<-1<<"\n";
			else {
				cout<<dq.front()<<"\n";
				dq.pop_front();
			}
		} else if(m=="pop_back") {
			if(dq.empty()) cout<<-1<<"\n";
			else {
				cout<<dq.back()<<"\n";
				dq.pop_back();
			}
		} else if(m=="size") {
			cout<<dq.size()<<"\n";
		} else if(m=="empty") {
			cout<<dq.empty()<<"\n";
		} else if(m=="front") {
			if(dq.empty()) cout<<-1<<"\n";
			else cout<<dq.front()<<"\n";
		} else if(m=="back") {
			if(dq.empty()) cout<<-1<<"\n";
			else cout<<dq.back()<<"\n";
		}
	}
}