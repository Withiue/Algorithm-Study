#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, param;
    cin >> n;
    stack<int> stk; // 정수 저장 스택 구현

    for (int i = 0; i < n; i++) {
        string func;
        cin >> func;
        if (func == "push") {
            cin >> param;
            stk.push(param);
        } else if (func == "pop") {
            if (stk.empty()) {
                cout << -1 << "\n";
            } else {
                cout << stk.top() << "\n";
                stk.pop();
            }
        } else if (func == "size") {
            cout << stk.size() << "\n";
        } else if (func == "empty") {
            cout << (stk.empty() ? 1 : 0) << "\n";
        } else if (func == "top") {
            if (stk.empty()) {
                cout << -1 << "\n";
            } else {
                cout << stk.top() << "\n";
            }
        }
    }

    return 0;
}
