#include <bits/stdc++.h>
using namespace std;
int main(void) {
	queue<int> Q;
	int n, a;
	string m;
	cin>>n;
	while(n--) {
		cin>>m;
		if(m=="push") {
			cin>>a;
			Q.push(a);
		} else if(m=="pop") {
			if(!Q.empty()) {
				cout<<Q.front()<<"\n";
				Q.pop();
			}
			else if(Q.empty()) cout<<-1<<"\n";
		} else if(m=="front") {
			if(!Q.empty()) cout<<Q.front()<<"\n";
			else if(Q.empty()) cout<<-1<<"\n";
		} else if(m=="back") {
			if(!Q.empty()) cout<<Q.back()<<"\n";
			else if(Q.empty()) cout<<-1<<"\n";
		} else if(m=="empty") {
			cout<<Q.empty()<<"\n";
		} else if(m=="size") {
			cout<<Q.size()<<"\n";
		}
	}
}