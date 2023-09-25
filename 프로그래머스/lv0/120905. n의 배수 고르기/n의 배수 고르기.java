import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int num : numlist) {
            if(num % n == 0) answer.add(num);
        }
        int[] int_answer = new int[answer.size()];
        for(int i = 0; i < answer.size(); i++) {
            int_answer[i] = answer.get(i);
        }
        return int_answer;
    }
}