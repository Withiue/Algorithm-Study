class Solution {
    public String solution(String my_string) {
        String answer = "";
        for(int i = 0; i < my_string.length(); i++) {
            if(!answer.contains(String.valueOf(my_string.charAt(i)))) { //answer에 i번째 문자가 없으면 (String끼리 비교해야 함)
                answer += my_string.charAt(i); //answer에 해당 문자 넣기
            }
        }
        return answer;
    }
}