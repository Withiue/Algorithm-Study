#include <bits/stdc++.h>
using namespace std;
int input[8];
int main() {
	int asc = 0;
	int des = 0;
	
	for (int i = 0; i < 8; i++) {
		cin >> input[i];
		if (input[i] == i+1) {
			asc++;
		} else if(input[i] == 8-i) {
			des++;
		} 
	}
	
	if(asc == 8) {
		cout << "ascending";
	} else if(des == 8) {
		cout << "descending";
	} else {
		cout << "mixed";
	}
	
}