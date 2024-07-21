#include <bits/stdc++.h>
using namespace std;
int a, b;
int gcd(int a, int b) {
	int t;
	while(b) {
		t=a % b; //나머지 
		a=b;
		b=t; //b에는 나머지만 들어감 
	}
	return a;
}
int lcm(int a, int b) {
	return a*b / gcd(a, b);
}
int main() {
	cin >> a >> b;
	cout << gcd(a, b) << '\n';
	cout << lcm(a, b) << '\n';
} 