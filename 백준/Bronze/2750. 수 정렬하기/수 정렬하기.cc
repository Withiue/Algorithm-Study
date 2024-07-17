#include <bits/stdc++.h>
using namespace std;
int main() {
	int n;
	cin >> n; // 배열 갯수 입력받기
	vector<int> array(n); //벡터 초기화 
	// 배열 요소 입력받기 
	int i;
	for (i=0; i<n; i++) {
		cin >> array[i];
	}
	// 오름차순
	sort(array.begin(), array.end()); 
	//오름차순 정렬된 배열 요소 출력하기
	for (i=0; i<n; i++) {
		cout << array[i] << "\n";
	}
}