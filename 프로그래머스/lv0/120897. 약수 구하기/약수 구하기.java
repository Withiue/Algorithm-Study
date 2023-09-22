import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if(n % i == 0) answer.add(i);
        }
        int[] intAnswer = new int[answer.size()];
        for(int j = 0; j < answer.size(); j++) {
            intAnswer[j] = answer.get(j);
        }
        return intAnswer;
    }
}