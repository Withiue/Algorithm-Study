import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length]; // 순서 배열
        for(int i = 0; i < emergency.length; i++) { // 자신보다 높은 값이 있으면 순서배열에 +1
            for (int j = 0; j < emergency.length; j++) {
                if(emergency[i] < emergency[j]) {
                    answer[i]++;
                }
            }
            answer[i]++;
        }         
        return answer;
    }
}

/*
Stream, Arrays, Collections 등을 배워야겠다.
*/