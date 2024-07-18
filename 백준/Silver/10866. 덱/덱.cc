#include <bits/stdc++.h>
using namespace std;
int N, X;
string func;
deque<int> dq;
int main() {
	cin >> N;
	for (int i=0; i<N; i++) {
		cin >> func;
		if (func == "push_front") {
			//push_front X: 정수 X를 덱의 앞에 넣는다.
			cin >> X;
			dq.push_front(X);
		} else if (func == "push_back") {
			//push_back X: 정수 X를 덱의 뒤에 넣는다.
			cin >> X;
			dq.push_back(X);
		} else if (func == "pop_front") {
			//pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (dq.empty()){
				cout << -1 << "\n";
			} else {
				cout << dq.front() << "\n";
				dq.pop_front();
			}
		} else if (func == "pop_back") {
			//pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (dq.empty()){
				cout << -1 << "\n";
			} else {
				cout << dq.back() << "\n";
				dq.pop_back();
			}
		} else if (func == "size") {
			//size: 덱에 들어있는 정수의 개수를 출력한다.
			cout << dq.size() << "\n";
		} else if (func == "empty") {
			//empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
			if (dq.empty()){
				cout << 1 << "\n";
			} else {
				cout << 0 << "\n";
			}
		} else if (func == "front") {
			//front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (dq.empty()){
				cout << -1 << "\n";
			} else {
				cout << dq.front() << "\n";
			}
		} else if (func == "back") {
			//back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
			if (dq.empty()){
				cout << -1 << "\n";
			} else {
				cout << dq.back() << "\n";
			}
		}
	}
	return 0;
}