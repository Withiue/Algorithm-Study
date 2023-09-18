class Solution {
    public int solution(int n) {
        int answer = 0;
        int factorial = 1;
        int i = 1;
        
        while (factorial <= n) {
            answer = i;
            i++;
            factorial *= i;
        }
        
        return answer;
    }
}