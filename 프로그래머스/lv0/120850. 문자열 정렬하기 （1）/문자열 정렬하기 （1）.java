import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        my_string = my_string.replaceAll("[^0-9]","");
        String[] arr = my_string.split("");
        int[] answer = new int[arr.length];
        
        for(int i = 0; i < arr.length; i++) {
            answer[i] = Integer.parseInt(arr[i]);
        }
        Arrays.sort(answer);
            
        return answer;
    }
}