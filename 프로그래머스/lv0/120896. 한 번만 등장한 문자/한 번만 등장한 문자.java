import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arrS = s.split("");
        Arrays.sort(arrS);
        for(int i = 0; i < arrS.length; i++) {
            int cnt = 0;
            for(int j = 0; j < arrS.length; j++) {
                if(arrS[i].contains(arrS[j])) {
                    cnt++;
                }
            }
            if(cnt == 1) {
                answer += arrS[i];
            }
        }
        return answer;
    }
}