#include <string>
#include <vector>
#include <iostream>

using namespace std;

int answer = 0;

int calculate(string current, vector<int> numbers) {
    // +, - 계산하기
    int result = 0;
    for(int i = 0; i < numbers.size(); i++) {
        // + 이면
        if(current[i] == '+') {
            result += numbers[i];  
        } else { // - 이면
            result -= numbers[i];
        }
    }
    return result;
}

// 재귀
void recur(string current, int remaining, int target, vector<int> numbers) {
    int result = 0;
    // 다 뽑으면 멈추기, target과 같으면 answer값 +1
    if(remaining == 0) {
        result = calculate(current, numbers);
        if(result == target) {
            answer++;
            return;    
        } else {
            return;
        }
    }
    
    // 재귀 파트
    // + 뽑기
    recur(current + "+", remaining - 1, target, numbers);
    // - 뽑기
    recur(current + "-", remaining - 1, target, numbers);
}

int solution(vector<int> numbers, int target) {
    recur("", numbers.size(), target, numbers); // length()는 string 전용. vector는 size()를 사용해야 한다.
    return answer;
}