#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0); cin.tie(0);
	int N, M, want;
	deque<int> DQ;
	int ans=0;
	cin>>N>>M;
	for(int i=1; i<=N; i++) DQ.push_back(i);
	while(M--) {
		cin>>want;
		int idx = find(DQ.begin(), DQ.end(), want) - DQ.begin(); //idx: want가 있는 위치
		while(DQ.front() != want) {
			if(idx < DQ.size() - idx) {
				//왼쪽으로 가
				DQ.push_back(DQ.front());
				DQ.pop_front();
			} else {
				//오른쪽으로 가
				DQ.push_front(DQ.back());
				DQ.pop_back();
			}
			ans++;
		}
		DQ.pop_front();
	}
	cout<<ans;
}