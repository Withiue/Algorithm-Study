/*pseudocode
7조각을 기준으로 경우의 수를 나눈다.
1. 1-7명일때 필요한 피자 수 = 1
2. 8명 이상일 때
    2-1. 7의 배수일 때 = n / 7
    2-2. 7의 배수가 아닐 때 = n / 7 + 1
*/

class Solution {
    public int solution(int n) {
        int pizzaNum = 0;
        if(n <= 7) {
            pizzaNum = 1;
        } else if(n % 7 == 0) {
            pizzaNum = n / 7;
        } else {
            pizzaNum = n / 7 + 1;
        }
        
        return pizzaNum;
    }
}