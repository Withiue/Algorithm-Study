class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for(String firstStr : s1) {
            for(String secondStr : s2) {
                if(firstStr.equals(secondStr)) answer++;
            }
        }
        return answer;
    }
}