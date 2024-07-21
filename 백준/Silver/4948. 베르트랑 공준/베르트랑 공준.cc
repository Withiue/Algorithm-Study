#include <bits/stdc++.h>
using namespace std;
const int Max = 123456 * 2; //소수를 찾을 최대 범위 

int main() {
	bool arr[Max + 1] = {false}; //false면 소수, 일단 모두 소수라고 가정 
	arr[1] = true; //1은 항상 소수가 아님 
	
	//에라토스테네스의 체 알고리즘 
	for (int i=2; i*i <= Max; ++i) {
		if (!arr[i]) { // 현재 숫자가 소수인지 판별한다.  
			for (int j = 2; i*j <= Max; ++j) { //소수의 배수들(소수 아님)을 체에 거른다. 
				arr[i*j] = true;
			}
		}
	} 
	
	//사용자 입력 및 소수 개수 세기 
	int ch;
	cin >> ch;
	while(ch) { //0을 입력하면 종료 
		int count = 0;
		for(int i=ch+1; i <= 2 * ch; ++i) {
			if (!arr[i]) ++count; //false의 개수 세기 
		}
		cout << count << '\n';
		cin >> ch;
	}
}