class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] strSplit = my_string.split("[a-zA-Z]"); //알파벳 기준으로 쪼개지니까 연속된 자연수가 각각 잘리지 않고 뭉텅이로 잘림
        
        for(int i = 0; i < strSplit.length; i++) {
            if(!strSplit[i].isEmpty()) {
                answer += Integer.parseInt(strSplit[i]);
            }
        }
        
        return answer;
    }
}