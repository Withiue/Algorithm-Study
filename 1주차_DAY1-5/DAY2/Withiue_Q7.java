/*pseudocode
1. 두 분수를 통분해 더한다.
2. 1의 분자와 분모를 둘의 최대공약수로 나눈다.(둘이 같은 값으로 나눠서 나머지가 0이면 공약수)
*/

class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numer3 = numer1 * denom2 + numer2 * denom1; //분자
        int denom3 = denom1 * denom2; //분모
        
        //최대공약수
        int max = 1;
        
        for(int i=1; i <= numer3; i++) {
            if(numer3 % i == 0 && denom3 % i == 0) {
                max = i;
            }
        }
        int[] answer = {numer3/ max, denom3/ max};
        
        return answer;
    }
}