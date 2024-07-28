#include<bits/stdc++.h>
using namespace std;

long long songToBit[11]; // 기타가 어떤 노래를 재생할 수 있는지를 비트로 저장
int n, m; // n: 기타의 수, m: 노래의 수
int ans = 0x3f3f3f3f; // 최소 기타 수를 저장할 변수, 큰 값으로 초기화
int maxCnt = 0; // 재생할 수 있는 최대 노래 수를 저장

int countBit(long long bit) {
    int cnt = 0;
    while(bit) {
        cnt += bit & 1; // 최하위 비트가 1인지 확인하여 cnt 증가
        bit >>= 1; // 비트를 오른쪽으로 한 칸 이동
    }
    return cnt;
}

void solve(int idx, long long bit, int cnt) {
    int bitToSong = countBit(bit); // 현재 비트로 재생할 수 있는 노래 수 계산

    if(bitToSong > maxCnt) { // 더 많은 노래를 재생할 수 있다면
        maxCnt = bitToSong; // 최대 재생 가능한 노래 수 업데이트
        ans = cnt; // 최소 기타 수 업데이트
    } else if (bitToSong == maxCnt) { // 최대 재생 가능한 노래 수가 같다면
        ans = min(ans, cnt); // 최소 기타 수를 더 작은 값으로 업데이트
    }

    if(idx == n) return; // 기타를 다 탐색했다면 반환

    solve(idx+1, bit | songToBit[idx], cnt+1); // 현재 기타를 사용하는 경우
    solve(idx+1, bit, cnt); // 현재 기타를 사용하지 않는 경우
}

int main() {
    ios_base::sync_with_stdio(false); // C++ 표준 입출력과 C 표준 입출력의 동기화를 비활성화하여 성능 향상
    cout.tie(0); // cout과 cin의 묶음을 해제하여 성능 향상
    cin.tie(0); // cin과 cout의 묶음을 해제하여 성능 향상
    
    cin >> n >> m; // 기타 수와 노래 수 입력받기

    for(int i = 0; i < n; i++) {
        string name, detail;
        cin >> name >> detail; // 기타의 이름과, 각 기타가 어떤 노래를 재생할 수 있는지 입력받기
        for(int j = 0; j < m; j++) {
            if(detail[j] == 'Y') { // 노래를 재생할 수 있다면
                songToBit[i] |= (1LL << (m-1-j)); // 비트로 저장
            }
        }
    }

    solve(0, 0, 0); // 모든 조합을 탐색

    if(!maxCnt) cout << -1; // 재생 가능한 노래가 없다면 -1 출력
    else cout << ans; // 최소 기타 수 출력
}
