/*
필요한 개미 수, 남은 hp 구하기
*/
class Solution {
    public int solution(int hp) {
        int answer = 0;
        int tempAnt = 0;
        for(int i = 5; i >= 1; i -= 2) {
            tempAnt = hp / i; //필요한 개미 수
            answer += tempAnt;
            hp -= i * tempAnt; // 남은 hp
        }
        return answer;
    }
}