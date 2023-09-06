/*pseudocode
1. 오름차순으로 정렬한다.
이중 for문으로 정렬한다.
2. 중앙값을 구한다.
중앙값 인덱스 = 배열 길이 / 2 (인덱스값은 0부터 시작하기 때문에 +1을 할 필요가 없다.)
*/

class Solution {
    public int solution(int[] array) {
        
        for(int j=0; j < array.length; j++) {
            for(int i=0; i < array.length - 1; i++) {
                if(array[i] > array[i+1]) {
                    int temp = 0;
                    temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
            }
        }

        int mid = (array.length / 2);
        return array[mid];
    }
}