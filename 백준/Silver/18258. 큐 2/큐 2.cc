#include <bits/stdc++.h>
using namespace std;
int n;
int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	cin>>n;
	queue<int> Q;
	while(n--) {
		string m;
		cin>>m;
		int a;
		if(m=="push") {
			cin>>a;
			Q.push(a);
		} else if(m=="pop") {
			if(Q.empty()) cout<<-1<<"\n";
			else {
				cout<<Q.front()<<"\n";
				Q.pop();
			}
		} else if(m=="size") {
			cout<<Q.size()<<"\n";
		} else if(m=="empty") {
			if(Q.empty()) cout<<1<<"\n";
			else cout<<0<<"\n";
		} else if(m=="front") {
			if(Q.empty()) cout<<-1<<"\n";
			else cout<<Q.front()<<"\n";
		} else if(m=="back") {
			if(Q.empty()) cout<<-1<<"\n";
			else cout<<Q.back()<<"\n";
		}
	}
}