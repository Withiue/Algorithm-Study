/*pseudocode
n명이서 i판을 시켰을때의 피자 조각 갯수 = i * 6
갯수가 n으로 나누어 떨어지면 그때의 가장 작은 i값 구하기
*/

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i=1; i <= n; i++) {
            if(i * 6 % n == 0) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}