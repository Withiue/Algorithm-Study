class Solution {
    public int solution(int[] array, int n) {
        int answer = 100; // 최종 차이 구하기(절댓값이 제일 작아야함)
        for(int num : array) {
            int diff = num - n; // array 내에서 차이 구하기(answer와 비교대상)
            if(Math.abs(diff) < Math.abs(answer)) {
                answer = diff;
            } else if(Math.abs(diff) == Math.abs(answer) && diff < 0) { // 차이 절댓값 같을때 diff가 음수면?
                answer = diff;
            }
        }
        return answer + n; // 차이 + 주어진 정수
    }
}