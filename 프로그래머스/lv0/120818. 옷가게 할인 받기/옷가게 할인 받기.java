/*pseudocode
1. 10원 이상 10만원 미만일때 할인율 0%
2. 10만원 이상 30만원 미만일때 할인율 5%
3. 30만원 이상 50만원 미만일때 할인율 10%
4. 50만원 이상일때 할인율 20%
최종가 = 옷의 가격 * (1-할인율*0.01)
*/

class Solution {
    public int solution(int price) {
        int answer = 0;
        if(10 <= price && price < 100000) {
            answer = price;
        } else if(100000 <= price && price < 300000) {
            answer = (int)(price * (1 - 5 * 0.01));
        } else if(300000 <= price && price < 500000) {
            answer = (int)(price * (1 - 10 * 0.01));
        } else {
            answer = (int)(price * (1 - 20 * 0.01));
        }
        
        return answer;
    }
}