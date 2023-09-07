/*pseudocode
1. 정수 배열의 값 다 더하기
2. 더한 값을 정수 배열의 길이로 나누기(실수 자료형에 담을 것)
*/

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int sum = 0;
        for(int i=0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        answer = (double)sum / numbers.length;
        return answer;
    }
}