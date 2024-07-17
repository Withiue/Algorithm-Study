#include <bits/stdc++.h>
using namespace std;
int N, param;
string func;
queue<int> q;
int main() {
	cin >> N;
	for(int i=0; i<N; i++) {
		cin >> func;
		if (func == "push") {
			//push X: 정수 X를 큐에 넣는 연산이다.
			cin >> param;
			q.push(param);
		} else if (func == "pop") {
			//pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (q.empty()) { //큐가 비었으면 -1 출력 
				cout << -1 << "\n";
			} else {
				cout << q.front() << "\n";
				q.pop();
			}
		} else if (func == "size") {
			//size: 큐에 들어있는 정수의 개수를 출력한다.
			cout << q.size() << "\n";
		} else if (func == "empty") {
			//empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
			if (q.empty()) {
				cout << 1 << "\n";
			} else {
				cout << 0 << "\n";
			}
		} else if (func == "front") {
			//front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (q.empty()) {
				cout << -1 << "\n";
			} else {
				cout << q.front() << "\n";
			}
		} else if (func == "back") {
			//back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (q.empty()) {
				cout << -1 << "\n";
			} else {
				cout << q.back() << "\n";
			}
		}
	}
	return 0;
} 