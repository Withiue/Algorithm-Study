class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        for(int i = 0; i < num_list.length; i++) {
            if(num_list[i] % 2 == 0) { //만약 짝수라면
                answer[0]++;
            } else { //만약 홀수라면
                answer[1]++;
            }
        }
        return answer;
    }
}