import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();

        for(int i = 2; i <= n; i++) {
            while(n % i == 0) {
                if(!answer.contains(i)) {
                    answer.add(i);
                    
                }
		        n /= i;
            }
        }
        
        int[] int_answer = new int[answer.size()];
        
        for(int j = 0; j < answer.size(); j++) {
            int_answer[j] = answer.get(j);
        }
        
        return int_answer;
    }
}