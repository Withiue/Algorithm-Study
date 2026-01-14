#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string ans = ""; // 스택 역할
    
    for (char c : number) {
        // 1. 스택이 비어있지 않고
        // 2. 아직 제거할 횟수(k)가 남았으면
        // 3. 스택의 마지막 글자가 현재 숫자보다 작으면 제거
        while (!ans.empty() && k > 0 && ans.back() < c) {
            ans.pop_back();
            k--;
        }
        ans.push_back(c);
    }
    
    // 예외 처리: k가 남은 경우 (ex: "987", k=1)
    // 이미 내림차순 정렬이 되어 pop이 안 일어났으므로 뒤에서부터 k개를 자름
    while (k > 0) {
        ans.pop_back();
        k--;
    }
    return ans;
}