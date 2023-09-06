/*pseudocode
이차원 배열을 활용한다.
array의 숫자를 종류별로 하나씩만 넣을 numArr를 만든다. 제한사항에 따라 크기는 1000으로 한다. 0~999까지의 숫자가 올 수 있기 때문.
즉 0~999의 값을 가지고 있는 배열 numArr를 만든다.
numArr에 array를 하나씩 뒤져가며 array[i]의 값에 따라 numArr에 해당 숫자를 +1 한다. (갯수 세기)
numArr를 오름차순으로 sort한다.
numArr[0]이 최빈값이다.
만약 numArr[0]과 numArr[1]이 같으면 최빈값이 여러 개이므로 -1을 return한다.
*/

class Solution {
    public int solution(int[] array) {
        int[] numArr = new int[1001];
        int answer = 0;
        
        for(int i = 0; i < array.length; i++) {
            for(int m = 0; m < 1000; m++) {
                if(array[i] == m) {
                    numArr[m] += 1;
                }
            }
        }
        
        int max = 0; // 몇 번 나왔는지
        for(int a = 0; a < numArr.length; a++) {
            if(numArr[a] > max) {
                max = numArr[a];
                answer = a;
            }
        }

        int maxNum = 0; // 최빈값 갯수
        for(int b = 0; b < numArr.length; b++) {
            if(numArr[b] == max) {
                maxNum++;
            }
            if (maxNum > 1) {
                return -1;
            }
        }
        return answer;
    }
}