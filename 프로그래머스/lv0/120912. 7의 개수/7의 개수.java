class Solution {
    public int solution(int[] array) {
        int cnt = 0;
        for(int i = 0; i < array.length; i++) {
            String strArr = Integer.toString(array[i]);
            char[] charArr = strArr.toCharArray();
            for(char n : charArr) {
                if(n == '7') cnt++;
            }
        }
        return cnt;
    }
}