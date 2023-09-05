/*pseudocode
1. for문으로 정수 배열의 갯수만큼 돌린다.
2. numbers의 각 원소에 두배를 해서 넣는다.
3. numbers를 return한다.
*/

class Solution {
    public int[] solution(int[] numbers) {
        for(int i=0; i<numbers.length; i++){
            numbers[i] *= 2;
        }
        return numbers;
    }
}