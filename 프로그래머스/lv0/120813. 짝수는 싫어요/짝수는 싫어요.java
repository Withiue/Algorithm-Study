/*pseudocode
1. n/2개인 answer 배열을 만든다.
2. for문을 돌리며 나머지가 1인 수들만 answer 배열에 차례대로 집어넣는다.
*/

class Solution {
    public int[] solution(int n) {
        int[] answer;
        
        if(n % 2 == 0) {
            answer = new int[n / 2];
        } else {
            answer = new int[(n / 2) +1];
        }

        
        int aIndex = 0;
        for(int i = 1; i < n+1; i++) {
            if(i % 2 == 1) {
                answer[aIndex] = i;
                aIndex++;
            }
        }
        
        return answer;
    }
}